from django.contrib.auth.models import User
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.authentication import JWTAuthentication
from auth_sys.models import CustomUser, Role
from auth_sys.permissions import IsAdminLevel2OrAbove, IsSuperAdmin, IsStudent
from events.signals.book_reservation_signals import *
from events.signals.custom_function_signals import book_issue_requested
from events.signals.degree_program_signals import degree_program_all_show_requested, degree_program_delete_requested, \
    degree_program_update_requested, degree_program_add_requested, degree_program_show_requested
from events.signals.qr_signals import student_qr_scan_requested, student_qr_scan_txt_requested
from events.signals.signals import *
from events.signals.faculty_signals import *
from events.signals.department_signals import *
from events.signals.course_signals import *
from events.signals.book_signals import *
from events.signals.center_signals import *
from events.signals.degree_program_course_signals import *
from events.signals.student_course_signals import *
from events.signals.center_book_signals import *
from events.signals.received_book_signals import *
from events.signals.district_signals import *
from events.signals.auth_signals.user_signals import *


class RegisterAPIView(APIView):
    def post(self, request):
        response_holder = {}

        def callback(result):
            response_holder.update(result)

        # publish raw request data
        user_register_requested.send(
            self.__class__,
            data=request.data,
            callback=callback
        )
        # return whatever the dispatch system send back

        if response_holder.get("success"):
            return Response(response_holder, status=status.HTTP_200_OK)
        else:
            return Response(response_holder, status=status.HTTP_400_BAD_REQUEST)


class LoginAPIView(APIView):
    def post(self, request):
        response_holder = {}

        def callback(result):
            response_holder.update(result)

        # publish raw request data
        user_login_requested.send(
            self.__class__,
            data=request.data,
            callback=callback
        )
        # return whatever the auth system send back

        if response_holder.get("success"):
            return Response(response_holder, status=status.HTTP_201_CREATED)
        else:
            return Response(response_holder, status=status.HTTP_400_BAD_REQUEST)


class LogoutAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        refresh_token = request.data.get("refresh_token")
        response_holder = {}

        def callback(result):
            response_holder.update(result)

        # Send logout signal
        user_logout_requested.send(
            sender=self.__class__,
            callback=callback,
            user=request.user,
            refresh_token=refresh_token
        )

        if response_holder.get("success"):
            return Response(response_holder, status=status.HTTP_200_OK)
        else:
            return Response(response_holder, status=status.HTTP_400_BAD_REQUEST)


class PasswordResetRequestAPIView(APIView):
    def post(self, request):
        response_holder = {}

        def callback(result):
            response_holder.update(result)

        # send raw request data
        user_password_reset_requested.send(
            self.__class__,
            data=request.data,
            callback=callback

        )
        # return whatever the auth system send back
        if response_holder.get("success"):
            return Response(response_holder, status=status.HTTP_200_OK)
        else:
            return Response(response_holder, status=status.HTTP_404_NOT_FOUND)


class PasswordResetConfirmAPIView(APIView):
    def post(self, request):
        response_holder = {}

        def callback(result):
            response_holder.update(result)

        # sent raw data to the
        user_password_reset_confirm_requested.send(
            sender=self.__class__,
            data=request.data,
            callback=callback,
        )

        # send whatever that auth system return
        if response_holder.get("success"):
            return Response(response_holder, status=status.HTTP_200_OK)
        else:
            return Response(response_holder, status=status.HTTP_400_BAD_REQUEST)


class AllUsersAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        response_holder = {}

        def callback(result):
            response_holder.update(result)

        user_all_show_requested.send(sender=self.__class__, callback=callback)

        return Response(
            response_holder,
            status=status.HTTP_200_OK if response_holder.get("success") else status.HTTP_400_BAD_REQUEST
        )


class UserAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, pk):  # pk comes from URL
        response_holder = {}

        def callback(result):
            response_holder.update(result)

        user_show_requested.send(sender=self.__class__, callback=callback, user_id=pk)

        return Response(
            response_holder,
            status=status.HTTP_200_OK if response_holder.get("success") else status.HTTP_400_BAD_REQUEST
        )


class AddUserAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        response_holder = {}

        def callback(result):
            response_holder.update(result)

        user_add_requested.send(sender=self.__class__, data=request.data, callback=callback)

        return Response(
            response_holder,
            status=status.HTTP_201_CREATED if response_holder.get("success") else status.HTTP_400_BAD_REQUEST
        )


class UpdateUserAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def put(self, request, pk):
        response_holder = {}

        def callback(result):
            response_holder.update(result)

        user_update_requested.send(
            sender=self.__class__,
            pk=pk,
            data=request.data,
            callback=callback
        )

        # Safety if no service responded
        if not response_holder:
            response_holder = {
                "success": False,
                "message": "Update service not available"
            }

        return Response(
            response_holder,
            status=status.HTTP_200_OK if response_holder.get("success") else status.HTTP_400_BAD_REQUEST
        )


class DeleteUserAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def delete(self, request, pk):
        response_holder = {}

        def callback(result):
            response_holder.update(result)

        user_delete_requested.send(
            sender=self.__class__,
            callback=callback,
            pk=pk
        )

        return Response(
            response_holder,
            status=status.HTTP_200_OK if response_holder.get("success") else status.HTTP_400_BAD_REQUEST
        )


class StudentRegAPIView(APIView):
    permission_classes = [IsAuthenticated]  # Only superadmin

    def post(self, request):
        data = request.data
        response_holder = {}

        # Trigger the signal which will handle all creation
        def callback(result):
            response_holder.update(result)

        student_registration_requested.send(
            sender=self.__class__,
            data=data,
            callback=callback
        )

        # Return whatever the signal sends back
        if response_holder.get("success"):
            return Response(response_holder, status=status.HTTP_201_CREATED)
        return Response(response_holder or {"success": False, "error": "Student registration failed"},
                        status=status.HTTP_400_BAD_REQUEST)


class StudentUpdateAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def put(self, request, pk):
        response_holder = {}
        print(request.data)

        def callback(result):
            response_holder.update(result)

        student_update_requested.send(
            sender=self.__class__,
            data=request.data,
            callback=callback,
            pk=pk,
        )

        # send back to the user whatever dispatch system send
        if response_holder.get("success"):
            return Response(response_holder, status=status.HTTP_200_OK)
        else:
            return Response(response_holder, status=status.HTTP_400_BAD_REQUEST)


class AllStudentAPIView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        response_holder = {}

        def callback(result):
            response_holder.update(result)

        # Send the signal to your listener/service
        student_all_requested.send(
            sender=self.__class__,
            callback=callback,
        )

        # send back to the user whatever dispatch system send
        if response_holder.get("success"):
            return Response(response_holder, status=status.HTTP_200_OK)
        else:
            return Response(response_holder, status=status.HTTP_400_BAD_REQUEST)


class StudentAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, pk):
        response_holder = {}

        def callback(result):
            response_holder.update(result)

        student_requested.send(
            sender=self.__class__,
            data=request,
            callback=callback,
            pk=pk,
        )

        # send back to the user whatever dispatch system send
        if response_holder.get("success"):
            return Response(response_holder, status=status.HTTP_200_OK)
        else:
            return Response(response_holder, status=status.HTTP_400_BAD_REQUEST)


class StudentDeleteAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def delete(self, request, pk):
        response_holder = {}

        def callback(result):
            response_holder.update(result)

        student_delete_requested.send(
            sender=self.__class__,
            callback=callback,
            pk=pk,
        )

        # send back to the user whatever dispatch system send
        if response_holder.get("success"):
            return Response(response_holder, status=status.HTTP_200_OK)
        else:
            return Response(response_holder, status=status.HTTP_400_BAD_REQUEST)


class AllFacultiesAPIView(APIView):
    permission_classes = [IsAuthenticated]

    # authentication_classes = [JWTAuthentication]

    def get(self, request):
        response_holder = {}

        def callback(results):
            response_holder.update(results)

        faculty_all_show_requested.send(
            sender=self.__class__,
            callback=callback
        )
        # send back to the user whatever dispatch system send
        if response_holder.get("success"):
            return Response(response_holder, status=status.HTTP_200_OK)
        else:
            return Response(response_holder, status=status.HTTP_400_BAD_REQUEST)


class AddFacultyAPIView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request):
        response_holder = {}

        def callback(results):
            response_holder.update(results)

        faculty_add_requested.send(
            sender=self.__class__,
            data=request.data,
            callback=callback
        )
        # send back to the user whatever dispatch system send
        print(response_holder)
        if response_holder.get("success"):
            return Response(response_holder, status=status.HTTP_201_CREATED)
        else:
            return Response(response_holder, status=status.HTTP_400_BAD_REQUEST)


class FacultyAPIView(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]

    def get(self, request, pk):
        response_holder = {}

        def callback(results):
            response_holder.update(results)

        faculty_show_requested.send(
            sender=self.__class__,
            data=request.data,
            callback=callback,
            pk=pk
        )

        if response_holder.get("success"):
            return Response(response_holder, status=status.HTTP_200_OK)
        else:
            return Response(response_holder, status=status.HTTP_400_BAD_REQUEST)


class UpdateFacultyAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def put(self, request, pk):
        response_holder = {}

        def callback(results):
            response_holder.update(results)

        faculty_update_requested.send(
            sender=self.__class__,
            data=request.data,
            callback=callback,
            pk=pk
        )

        if response_holder.get("success"):
            return Response(response_holder, status=status.HTTP_200_OK)
        else:
            return Response(response_holder, status=status.HTTP_400_BAD_REQUEST)


class DeleteFacultyAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def delete(self, request, pk):
        response_holder = {}

        def callback(results):
            response_holder.update(results)

        faculty_delete_requested.send(
            sender=self.__class__,
            data=request.data,
            callback=callback,
            pk=pk
        )

        if response_holder.get("success"):
            return Response(response_holder, status=status.HTTP_200_OK)
        else:
            return Response(response_holder, status=status.HTTP_400_BAD_REQUEST)


class AllDepartmentsAPIView(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]

    def get(self, request):
        response_holder = {}

        def callback(results):
            response_holder.update(results)

        department_all_show_requested.send(
            sender=self.__class__,
            callback=callback
        )

        if response_holder.get("success"):
            return Response(response_holder, status=status.HTTP_201_CREATED)
        else:
            return Response(response_holder, status=status.HTTP_400_BAD_REQUEST)


class DepartmentAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, pk):
        response_holder = {}

        def callback(results):
            response_holder.update(results)

        department_show_requested.send(
            sender=self.__class__,
            data=request.data,
            callback=callback,
            pk=pk
        )

        if response_holder.get("success"):
            return Response(response_holder, status=status.HTTP_200_OK)
        else:
            return Response(response_holder, status=status.HTTP_400_BAD_REQUEST)


class AddDepartmentAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        response_holder = {}

        def callback(results):
            response_holder.update(results)

        department_add_requested.send(
            sender=self.__class__,
            data=request.data,
            callback=callback
        )

        if response_holder.get("success"):
            return Response(response_holder, status=status.HTTP_201_CREATED)
        else:
            return Response(response_holder, status=status.HTTP_400_BAD_REQUEST)


class UpdateDepartmentAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def put(self, request, pk):
        response_holder = {}

        def callback(results):
            response_holder.update(results)

        department_update_requested.send(
            sender=self.__class__,
            data=request.data,
            callback=callback,
            pk=pk
        )

        if response_holder.get("success"):
            return Response(response_holder, status=status.HTTP_200_OK)
        else:
            return Response(response_holder, status=status.HTTP_400_BAD_REQUEST)


class DeleteDepartmentAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def delete(self, request, pk):
        response_holder = {}

        def callback(results):
            response_holder.update(results)

        department_delete_requested.send(
            sender=self.__class__,
            data=request.data,
            callback=callback,
            pk=pk
        )

        if response_holder.get("success"):
            return Response(response_holder, status=status.HTTP_200_OK)
        else:
            return Response(response_holder, status=status.HTTP_400_BAD_REQUEST)


# -------------------------------------------------->>>>>>>>>>>>>>>>>


class AllDegreeProgramsAPIView(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]

    def get(self, request):
        response_holder = {}

        def callback(results):
            response_holder.update(results)

        degree_program_all_show_requested.send(
            sender=self.__class__,
            callback=callback
        )

        if response_holder.get("success"):
            return Response(response_holder, status=status.HTTP_200_OK)
        else:
            return Response(response_holder, status=status.HTTP_400_BAD_REQUEST)


class DegreeProgramAPIView(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]

    def get(self, request, pk):
        response_holder = {}

        def callback(results):
            response_holder.update(results)

        degree_program_show_requested.send(
            sender=self.__class__,
            data=request.data,
            callback=callback,
            pk=pk
        )

        if response_holder.get("success"):
            return Response(response_holder, status=status.HTTP_200_OK)
        else:
            return Response(response_holder, status=status.HTTP_400_BAD_REQUEST)


class AddDegreeProgramAPIView(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]

    def post(self, request):
        response_holder = {}

        def callback(results):
            response_holder.update(results)

        degree_program_add_requested.send(
            sender=self.__class__,
            data=request.data,
            callback=callback
        )

        if response_holder.get("success"):
            return Response(response_holder, status=status.HTTP_201_CREATED)
        else:
            return Response(response_holder, status=status.HTTP_400_BAD_REQUEST)


class UpdateDegreeProgramAPIView(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]

    def put(self, request, pk):
        response_holder = {}

        def callback(results):
            response_holder.update(results)

        degree_program_update_requested.send(
            sender=self.__class__,
            data=request.data,
            callback=callback,
            pk=pk
        )

        if response_holder.get("success"):
            return Response(response_holder, status=status.HTTP_200_OK)
        else:
            return Response(response_holder, status=status.HTTP_400_BAD_REQUEST)


class DeleteDegreeProgramAPIView(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]

    def delete(self, request, pk):
        response_holder = {}

        def callback(results):
            response_holder.update(results)

        degree_program_delete_requested.send(
            sender=self.__class__,
            data=request.data,
            callback=callback,
            pk=pk
        )

        if response_holder.get("success"):
            return Response(response_holder, status=status.HTTP_200_OK)
        else:
            return Response(response_holder, status=status.HTTP_400_BAD_REQUEST)


# -------------------------------------------------->>>>>>>>>>>>>>>>>

class AllCoursesAPIView(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]

    def get(self, request):
        response_holder = {}

        def callback(result):
            response_holder.update(result)

        course_all_show_requested.send(sender=self.__class__, callback=callback)

        return Response(
            response_holder,
            status=status.HTTP_200_OK if response_holder.get("success") else status.HTTP_400_BAD_REQUEST
        )


class CourseAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, pk):
        response_holder = {}

        def callback(result):
            response_holder.update(result)

        course_show_requested.send(
            sender=self.__class__,
            callback=callback,
            pk=pk
        )

        return Response(
            response_holder,
            status=status.HTTP_200_OK if response_holder.get("success") else status.HTTP_400_BAD_REQUEST
        )


class AddCourseAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        response_holder = {}

        def callback(result):
            response_holder.update(result)

        course_add_requested.send(
            sender=self.__class__,
            data=request.data,
            callback=callback
        )

        return Response(
            response_holder,
            status=status.HTTP_201_CREATED if response_holder.get("success") else status.HTTP_400_BAD_REQUEST
        )


class UpdateCourseAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def put(self, request, pk):
        response_holder = {}

        def callback(result):
            response_holder.update(result)

        course_update_requested.send(
            sender=self.__class__,
            data=request.data,
            callback=callback,
            pk=pk
        )

        return Response(
            response_holder,
            status=status.HTTP_200_OK if response_holder.get("success") else status.HTTP_400_BAD_REQUEST
        )


class DeleteCourseAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def delete(self, request, pk):
        response_holder = {}

        def callback(result):
            response_holder.update(result)

        course_delete_requested.send(
            sender=self.__class__,
            callback=callback,
            pk=pk
        )

        return Response(
            response_holder,
            status=status.HTTP_200_OK if response_holder.get("success") else status.HTTP_400_BAD_REQUEST
        )


# -------------------------------------------------->>>>>>>>>>>>>>>>>
class AllBooksAPIView(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]

    def get(self, request):
        response_holder = {}

        def callback(result):
            if result:
                response_holder.update(result)

        book_all_show_requested.send(sender=self.__class__, callback=callback)

        if not response_holder:
            response_holder = {"success": False, "data": [], "error": "No books found"}

        return Response(
            response_holder,
            status=status.HTTP_200_OK if response_holder.get("success") else status.HTTP_400_BAD_REQUEST
        )


class BookAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, pk):
        response_holder = {}

        def callback(result):
            response_holder.update(result)

        book_show_requested.send(
            sender=self.__class__,
            callback=callback,
            pk=pk,
        )

        # send back to the user whatever dispatch system send
        if response_holder.get("success"):
            return Response(response_holder, status=status.HTTP_200_OK)
        else:
            return Response(response_holder, status=status.HTTP_400_BAD_REQUEST)


class AddBookAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        response_holder = {}

        def callback(result): response_holder.update(result)

        book_add_requested.send(sender=self.__class__, data=request.data, callback=callback)
        return Response(response_holder, status=status.HTTP_201_CREATED if response_holder.get(
            "success") else status.HTTP_400_BAD_REQUEST)


class UpdateBookAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def put(self, request, pk):
        response_holder = {}

        def callback(result): response_holder.update(result)

        book_update_requested.send(sender=self.__class__, data=request.data, callback=callback, pk=pk)
        return Response(response_holder,
                        status=status.HTTP_200_OK if response_holder.get("success") else status.HTTP_400_BAD_REQUEST)


class DeleteBookAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def delete(self, request, pk):
        response_holder = {}

        def callback(result): response_holder.update(result)

        book_delete_requested.send(sender=self.__class__, callback=callback, pk=pk)
        return Response(response_holder,
                        status=status.HTTP_200_OK if response_holder.get("success") else status.HTTP_400_BAD_REQUEST)


# -------------------------------------------------->>>>>>>>>>>>>>>>>

class AllCentersAPIView(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]

    def get(self, request):
        response_holder = {}

        def callback(result): response_holder.update(result)

        center_all_show_requested.send(sender=self.__class__, callback=callback)
        return Response(response_holder,
                        status=status.HTTP_200_OK if response_holder.get("success") else status.HTTP_400_BAD_REQUEST)


class CenterAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, pk):
        response_holder = {}

        def callback(result): response_holder.update(result)

        center_show_requested.send(sender=self.__class__, callback=callback, pk=pk)
        return Response(response_holder,
                        status=status.HTTP_200_OK if response_holder.get("success") else status.HTTP_400_BAD_REQUEST)


class AddCenterAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        response_holder = {}

        def callback(result): response_holder.update(result)

        center_add_requested.send(sender=self.__class__, data=request.data, callback=callback)
        return Response(response_holder, status=status.HTTP_201_CREATED if response_holder.get(
            "success") else status.HTTP_400_BAD_REQUEST)


class UpdateCenterAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def put(self, request, pk):
        response_holder = {}

        def callback(result): response_holder.update(result)

        center_update_requested.send(sender=self.__class__, data=request.data, callback=callback, pk=pk)
        return Response(response_holder,
                        status=status.HTTP_200_OK if response_holder.get("success") else status.HTTP_400_BAD_REQUEST)


class DeleteCenterAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def delete(self, request, pk):
        response_holder = {}

        def callback(result): response_holder.update(result)

        center_delete_requested.send(sender=self.__class__, callback=callback, pk=pk)
        return Response(response_holder,
                        status=status.HTTP_200_OK if response_holder.get("success") else status.HTTP_400_BAD_REQUEST)


# -------------------------------------------------->>>>>>>>>>>>>>>>>


class AllDegreeProgramCoursesAPIView(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]

    def get(self, request):
        response_holder = {}

        def callback(result):
            response_holder.update(result)

        degree_program_course_all_show_requested.send(
            sender=self.__class__,
            callback=callback
        )

        return Response(
            response_holder,
            status=status.HTTP_200_OK if response_holder.get("success")
            else status.HTTP_400_BAD_REQUEST
        )


class DegreeProgramCourseAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, pk):
        response_holder = {}

        def callback(result):
            response_holder.update(result)

        degree_program_course_show_requested.send(
            sender=self.__class__,
            callback=callback,
            pk=pk
        )

        return Response(
            response_holder,
            status=status.HTTP_200_OK if response_holder.get("success")
            else status.HTTP_400_BAD_REQUEST
        )


class AddDegreeProgramCourseAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        response_holder = {}

        def callback(result):
            response_holder.update(result)

        degree_program_course_add_requested.send(
            sender=self.__class__,
            data=request.data,
            callback=callback
        )

        return Response(
            response_holder,
            status=status.HTTP_201_CREATED if response_holder.get("success")
            else status.HTTP_400_BAD_REQUEST
        )


class UpdateDegreeProgramCourseAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def put(self, request, pk):
        response_holder = {}

        def callback(result):
            response_holder.update(result)

        degree_program_course_update_requested.send(
            sender=self.__class__,
            data=request.data,
            callback=callback,
            pk=pk
        )

        return Response(
            response_holder,
            status=status.HTTP_200_OK if response_holder.get("success")
            else status.HTTP_400_BAD_REQUEST
        )


class DeleteDegreeProgramCourseAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def delete(self, request, pk):
        response_holder = {}

        def callback(result):
            response_holder.update(result)

        degree_program_course_delete_requested.send(
            sender=self.__class__,
            callback=callback,
            pk=pk
        )

        return Response(
            response_holder,
            status=status.HTTP_200_OK if response_holder.get("success")
            else status.HTTP_400_BAD_REQUEST
        )


# -------------------------------------------------->>>>>>>>>>>>>>>>>
# -------------------------------------------------->>>>>>>>>>>>>>>>>

class TestAPI(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        response_holder = {}

        def callback(results):
            response_holder.update(results)

        testAPI.send(
            sender=self.__class__,
            callback=callback,

        )

        if response_holder.get("success"):
            return Response(response_holder, status=status.HTTP_200_OK)
        else:
            return Response(response_holder, status=status.HTTP_400_BAD_REQUEST)


class ScanQRAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        # print(request.FILES)
        if "qr_image" not in request.FILES:
            return Response({"error": "QR image required"}, status=status.HTTP_400_BAD_REQUEST)

        qr_image = request.FILES["qr_image"]

        # Prepare a response holder for the callback
        response_holder = {}

        # Define the callback function that signal will call
        def callback(result):
            response_holder.update(result)

        # Send signal to handle QR scan
        student_qr_scan_requested.send(
            sender=self.__class__,
            callback=callback,
            qr_image=qr_image
        )

        # Return response based on callback
        return Response(
            response_holder,
            status=status.HTTP_200_OK if response_holder.get("success")
            else status.HTTP_400_BAD_REQUEST
        )


class ScanQRTXTAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        qr_text = request.data.get("qr_text")

        if not qr_text:
            return Response(
                {"success": False, "error": "QR text is required"},
                status=status.HTTP_400_BAD_REQUEST
            )

        response_holder = {}

        def callback(result):
            # result MUST be a dict
            if isinstance(result, dict):
                response_holder.update(result)

        # Fire signal
        student_qr_scan_txt_requested.send(
            sender=self.__class__,
            callback=callback,
            qr_text=qr_text
        )

        # Safety check (signal not handled)
        if not response_holder:
            return Response(
                {"success": False, "error": "QR scan service not available"},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )

        return Response(
            response_holder,
            status=status.HTTP_200_OK
            if response_holder.get("success")
            else status.HTTP_400_BAD_REQUEST
        )


class AllStudentCoursesAPIView(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]

    def get(self, request):
        response_holder = {}

        def callback(result): response_holder.update(result)

        student_course_all_show_requested.send(sender=self.__class__, callback=callback)
        return Response(response_holder,
                        status=status.HTTP_200_OK if response_holder.get("success") else status.HTTP_400_BAD_REQUEST)


class StudentCourseAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, pk):
        response_holder = {}

        def callback(result): response_holder.update(result)

        student_course_show_requested.send(sender=self.__class__, callback=callback, pk=pk)
        return Response(response_holder,
                        status=status.HTTP_200_OK if response_holder.get("success") else status.HTTP_400_BAD_REQUEST)


class AddStudentCourseAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        response_holder = {}

        def callback(result): response_holder.update(result)

        student_course_add_requested.send(sender=self.__class__, data=request.data, callback=callback)
        return Response(response_holder, status=status.HTTP_201_CREATED if response_holder.get(
            "success") else status.HTTP_400_BAD_REQUEST)


class UpdateStudentCourseAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def put(self, request, pk):
        response_holder = {}

        def callback(result): response_holder.update(result)

        student_course_update_requested.send(sender=self.__class__, data=request.data, callback=callback, pk=pk)
        return Response(response_holder,
                        status=status.HTTP_200_OK if response_holder.get("success") else status.HTTP_400_BAD_REQUEST)


class DeleteStudentCourseAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def delete(self, request, pk):
        response_holder = {}

        def callback(result): response_holder.update(result)

        student_course_delete_requested.send(sender=self.__class__, callback=callback, pk=pk)
        return Response(response_holder,
                        status=status.HTTP_200_OK if response_holder.get("success") else status.HTTP_400_BAD_REQUEST)


class AllCenterBooksAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        response_holder = {}

        def callback(results):
            response_holder.update(results)

        center_book_all_show_requested.send(
            sender=self.__class__,
            callback=callback
        )

        if response_holder.get("success"):
            return Response(response_holder, status=status.HTTP_200_OK)
        else:
            return Response(response_holder, status=status.HTTP_400_BAD_REQUEST)


class CenterBookAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, pk):
        response_holder = {}

        def callback(results):
            response_holder.update(results)

        center_book_show_requested.send(
            sender=self.__class__,
            data=request.data,
            callback=callback,
            pk=pk
        )

        if response_holder.get("success"):
            return Response(response_holder, status=status.HTTP_200_OK)
        else:
            return Response(response_holder, status=status.HTTP_400_BAD_REQUEST)


class AddCenterBookAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        response_holder = {}

        def callback(results):
            response_holder.update(results)

        center_book_add_requested.send(
            sender=self.__class__,
            data=request.data,
            callback=callback
        )

        if response_holder.get("success"):
            return Response(response_holder, status=status.HTTP_201_CREATED)
        else:
            return Response(response_holder, status=status.HTTP_400_BAD_REQUEST)


class UpdateCenterBookAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def put(self, request, pk):
        response_holder = {}

        def callback(results):
            response_holder.update(results)

        center_book_update_requested.send(
            sender=self.__class__,
            data=request.data,
            callback=callback,
            pk=pk
        )

        if response_holder.get("success"):
            return Response(response_holder, status=status.HTTP_200_OK)
        else:
            return Response(response_holder, status=status.HTTP_400_BAD_REQUEST)


class DeleteCenterBookAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def delete(self, request, pk):
        response_holder = {}

        def callback(results):
            response_holder.update(results)

        center_book_delete_requested.send(
            sender=self.__class__,
            data=request.data,
            callback=callback,
            pk=pk
        )

        if response_holder.get("success"):
            return Response(response_holder, status=status.HTTP_200_OK)
        else:
            return Response(response_holder, status=status.HTTP_400_BAD_REQUEST)


class AllReceivedBooksAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        response_holder = {}

        def callback(results): response_holder.update(results)

        received_book_all_show_requested.send(
            sender=self.__class__,
            callback=callback
        )

        return Response(response_holder,
                        status=status.HTTP_200_OK if response_holder.get("success") else status.HTTP_400_BAD_REQUEST)


class ReceivedBookAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, pk):
        response_holder = {}

        def callback(results): response_holder.update(results)

        received_book_show_requested.send(
            sender=self.__class__,
            data=request.data,
            callback=callback,
            pk=pk
        )

        return Response(response_holder,
                        status=status.HTTP_200_OK if response_holder.get("success") else status.HTTP_400_BAD_REQUEST)


class AddReceivedBookAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        response_holder = {}

        def callback(results): response_holder.update(results)

        received_book_add_requested.send(
            sender=self.__class__,
            data=request.data,
            callback=callback
        )

        return Response(response_holder, status=status.HTTP_201_CREATED if response_holder.get(
            "success") else status.HTTP_400_BAD_REQUEST)


class UpdateReceivedBookAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def put(self, request, pk):
        response_holder = {}

        def callback(results): response_holder.update(results)

        received_book_update_requested.send(
            sender=self.__class__,
            data=request.data,
            callback=callback,
            pk=pk
        )

        return Response(response_holder,
                        status=status.HTTP_200_OK if response_holder.get("success") else status.HTTP_400_BAD_REQUEST)


class DeleteReceivedBookAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def delete(self, request, pk):
        response_holder = {}

        def callback(results): response_holder.update(results)

        received_book_delete_requested.send(
            sender=self.__class__,
            callback=callback,
            pk=pk
        )

        return Response(response_holder,
                        status=status.HTTP_200_OK if response_holder.get("success") else status.HTTP_400_BAD_REQUEST)


class BookReservationCreateAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        response_holder = {}

        def callback(result): response_holder.update(result)

        book_reservation_add_requested.send(
            sender=self.__class__,
            data=request.data,
            callback=callback
        )

        return Response(
            response_holder,
            status=status.HTTP_201_CREATED if response_holder.get("success") else status.HTTP_400_BAD_REQUEST
        )


class BookReservationUpdateAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def put(self, request, pk):
        response_holder = {}

        def callback(result): response_holder.update(result)

        book_reservation_update_requested.send(
            sender=self.__class__,
            pk=pk,
            data=request.data,
            callback=callback
        )

        return Response(
            response_holder,
            status=status.HTTP_200_OK if response_holder.get("success") else status.HTTP_400_BAD_REQUEST
        )


class BookReservationDeleteAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def delete(self, request, pk):
        response_holder = {}

        def callback(result): response_holder.update(result)

        book_reservation_delete_requested.send(
            sender=self.__class__,
            pk=pk,
            callback=callback
        )

        return Response(
            response_holder,
            status=status.HTTP_200_OK if response_holder.get("success") else status.HTTP_404_NOT_FOUND
        )


class BookReservationDetailAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, pk):
        response_holder = {}

        def callback(result): response_holder.update(result)

        book_reservation_show_requested.send(
            sender=self.__class__,
            pk=pk,
            callback=callback
        )

        return Response(
            response_holder,
            status=status.HTTP_200_OK if response_holder.get("success") else status.HTTP_404_NOT_FOUND
        )


class BookReservationListAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        response_holder = {}

        def callback(result): response_holder.update(result)

        book_reservation_all_show_requested.send(
            sender=self.__class__,
            callback=callback
        )

        return Response(
            response_holder,
            status=status.HTTP_200_OK
        )


class DistrictCreateAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        response_holder = {}

        def callback(result): response_holder.update(result)

        district_add_requested.send(sender=self.__class__, data=request.data, callback=callback)
        return Response(response_holder, status=status.HTTP_201_CREATED if response_holder.get(
            "success") else status.HTTP_400_BAD_REQUEST)


class DistrictUpdateAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def put(self, request, pk):
        response_holder = {}

        def callback(result): response_holder.update(result)

        district_update_requested.send(sender=self.__class__, data=request.data, pk=pk, callback=callback)
        return Response(response_holder,
                        status=status.HTTP_200_OK if response_holder.get("success") else status.HTTP_400_BAD_REQUEST)


class DistrictDeleteAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def delete(self, request, pk):
        response_holder = {}

        def callback(result): response_holder.update(result)

        district_delete_requested.send(sender=self.__class__, pk=pk, callback=callback)
        return Response(response_holder,
                        status=status.HTTP_200_OK if response_holder.get("success") else status.HTTP_404_NOT_FOUND)


class DistrictDetailAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, pk):
        response_holder = {}

        def callback(result): response_holder.update(result)

        district_show_requested.send(sender=self.__class__, pk=pk, callback=callback)
        return Response(response_holder,
                        status=status.HTTP_200_OK if response_holder.get("success") else status.HTTP_404_NOT_FOUND)


class DistrictListAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        response_holder = {}

        def callback(result): response_holder.update(result)

        district_all_show_requested.send(sender=self.__class__, callback=callback)
        return Response(response_holder, status=status.HTTP_200_OK)


class IssueBookAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        response_holder = {}

        def callback(result):
            response_holder.update(result)

        # Trigger the signal with request data and the callback
        book_issue_requested.send(
            sender=self.__class__,
            data=request.data,
            callback=callback
        )

        # Determine status based on the success key returned by the service
        # If success is True, return 201 (Created), otherwise return 400 (Bad Request)
        http_status = status.HTTP_201_CREATED if response_holder.get("success") else status.HTTP_400_BAD_REQUEST

        return Response(response_holder, status=http_status)


class CreateStaffAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        response_holder = {}

        def callback(results):
            response_holder.update(results)

        create_staff_requested.send(
            sender=self.__class__,
            data=request.data,
            callback=callback
        )

        return Response(
            response_holder,
            status=status.HTTP_201_CREATED
            if response_holder.get("success")
            else status.HTTP_400_BAD_REQUEST
        )

class MakeBookReservationAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, uuid):
        response_holder = {}

        def callback(result):
            response_holder.update(result)

        make_book_reservation_requested.send(
            sender=self.__class__,
            callback=callback,
            user=request.user,
            uuid=uuid
        )

        # return response from dispatch system
        if response_holder.get("success"):
            return Response(response_holder, status=status.HTTP_200_OK)
        else:
            return Response(response_holder, status=status.HTTP_400_BAD_REQUEST)


class ViewCenterAllocationAPIView(APIView):
    pass


class DashboardAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        response_holder = {}

        def callback(results):
            response_holder.update(results)

        dashboard_show_requested.send(
            sender=self.__class__,
            callback=callback
        )

        return Response(
            response_holder,
            status=status.HTTP_200_OK if response_holder.get("success") else status.HTTP_400_BAD_REQUEST
        )
