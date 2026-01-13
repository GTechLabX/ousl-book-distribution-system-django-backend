from django.contrib.auth.models import User

from auth_sys.models import CustomUser, Role
from dispatch_sys.models import Student
from dispatch_sys.serializers.student_reg_serializers import StudentSerializer


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


def register_student(sender, data, callback, **kwargs):
    """
    Handles full student registration:
    1. Create Django User
    2. Create CustomUser with role STUDENT
    3. Create Student record using serializer
    """
    s_no = data.get("s_no")
    nic = data.get("nic")
    email = f"{s_no}@ousl.lk"
    username = nic
    password = nic  # default password

    # --- Check if user already exists ---
    if User.objects.filter(username=username).exists():
        return callback({"success": False, "error": "User already exists"})

    # --- Create Django User ---
    django_user = User.objects.create_user(username=username, email=email, password=password)

    # --- Create CustomUser ---
    custom_user, created = CustomUser.objects.get_or_create(user=django_user)
    custom_user.role = Role.STUDENT
    custom_user.save()

    # --- Create Student record via serializer ---
    data['custom_user'] = custom_user.id  # link student to CustomUser

    serializer = StudentSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return callback({
            "success": True,
            "username": django_user.username,
            "password": password,
            "message": "Student account created successfully",
            "student_id": serializer.data
        })
    else:
        return callback({
            "success": False,
            "errors": serializer.errors
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
