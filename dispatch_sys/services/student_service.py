from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.db import transaction

from auth_sys.models import CustomUser, Role
from dispatch_sys.models import Student
from dispatch_sys.serializers.student_reg_serializers import StudentSerializer
from events.signals.student_acc_created_signals import student_acc_created_required


def student_service(sender, data, callback, pk, **kwargs):
    try:
        student = Student.objects.get(pk=pk)
    except Student.DoesNotExist as e:
        return callback(
            {
                "success": False,
                "errors": str(e)
            }
        )
    serializer = StudentSerializer(student)

    return callback(
        {
            "success": True,
            "message": serializer.data
        }
    )


#
# def register_student(sender, data, callback, **kwargs):
#     """
#     Handles full student registration:
#     1. Create Django User
#     2. Create CustomUser with role STUDENT
#     3. Create Student record using serializer
#     """
#     s_no = data.get("s_no")
#     nic = data.get("nic")
#     email = f"{s_no}@ousl.lk"
#     username = nic
#     password = nic  # default password
#
#     # --- Check if user already exists ---
#     if User.objects.filter(username=username).exists():
#         return callback({"success": False, "error": "User already exists"})
#
#     # --- Create Django User ---
#     django_user = User.objects.create_user(username=username, email=email, password=password)
#
#     # --- Create CustomUser ---
#     custom_user, created = CustomUser.objects.get_or_create(user=django_user)
#     custom_user.role = Role.STUDENT
#     custom_user.save()
#
#     # --- Create Student record via serializer ---
#     data['custom_user'] = custom_user.id  # link student to CustomUser
#
#     serializer = StudentSerializer(data=data)
#     if serializer.is_valid():
#         serializer.save()
#         return callback({
#             "success": True,
#             "username": django_user.username,
#             "password": password,
#             "message": "Student account created successfully",
#             "student_id": serializer.data
#         })
#     else:
#         return callback({
#             "success": False,
#             "errors": serializer.errors
#         })


def register_student(sender, data, callback, **kwargs):
    try:
        with transaction.atomic():
            s_no = data.get("s_no")
            nic = data.get("nic")
            email = f"{s_no}@ousl.lk"
            username = nic
            password = nic

            # --- Check existing user ---
            if User.objects.filter(username=username).exists():
                raise ValidationError("User already exists")

            # --- Create Django User ---
            django_user = User.objects.create_user(
                username=username,
                email=email,
                password=password
            )

            # --- Create CustomUser ---
            custom_user, _ = CustomUser.objects.get_or_create(user=django_user)
            custom_user.role = Role.STUDENT
            custom_user.save()

            # --- Create Student ---
            data["custom_user"] = custom_user.id
            serializer = StudentSerializer(data=data)

            if not serializer.is_valid():
                raise ValidationError(serializer.errors)

            student = serializer.save()

            # --- Send Email (must raise error if fails) ---
            student_acc_created_required.send(
                sender=register_student,
                user_id=django_user.id,
                username=username,
                email=email,
                password=password
            )

            # If everything passed
            return callback({
                "success": True,
                "message": "Student account created successfully",
                "student_id": serializer.data
            })

    except Exception as e:
        #  Any error then full rollback
        return callback({
            "success": False,
            "error": str(e)
        })


def student_delete_service(sender, callback, pk, **kwargs):
    try:
        student = Student.objects.get(pk=pk)
    except Student.DoesNotExist as e:
        return callback({
            "success": False,
            "errors": f"Student with id {pk} does not exist"
        })

    # serialize before deletion if you want to return data
    serializer = StudentSerializer(student)
    student.delete()  # deletes the record

    return callback({
        "success": True,
        "message": "Student deleted successfully",
        "deleted_student": serializer.data  # returns deleted data
    })


def student_all_service(sender, callback, **kwargs):
    student = Student.objects.all()
    serializer = StudentSerializer(student, many=True)
    return callback(
        {
            "success": True,
            "message": serializer.data
        }
    )


def student_update_service(sender, data, callback, pk, **kwargs):
    print(data, pk)
    try:
        student = Student.objects.get(pk=pk)
    except Student.DoesNotExist as e:
        return callback({
            "success": False,
            "errors": f"Student with id {pk} does not exist"
        })

    serializer = StudentSerializer(student, data=data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return callback({
            "success": True,
            "message": serializer.data,
        })
    else:
        return callback({
            "success": False,
            "errors": serializer.errors
        })
