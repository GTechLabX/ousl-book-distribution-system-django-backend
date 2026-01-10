from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.authentication import JWTAuthentication

from events.signals.degree_program_signals import degree_program_all_show_requested, degree_program_delete_requested, \
    degree_program_update_requested, degree_program_add_requested, degree_program_show_requested
from events.signals.signals import *
from events.signals.faculty_signals import *
from events.signals.department_signals import *
from events.signals.course_signals import *
from events.signals.book_signals import *


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


class StudentRegAPIView(APIView):
    permission_classes = [IsAuthenticated]  # access with only register users

    def post(self, request):
        response_holder = {}

        def callback(result):
            response_holder.update(result)

        # publish raw request data
        student_registration_requested.send(
            sender=self.__class__,
            data=request.data,
            callback=callback
        )

        # return whatever the dispatch system send back

        if response_holder.get("success"):
            return Response(response_holder, status=status.HTTP_201_CREATED)
        else:
            return Response(response_holder, status=status.HTTP_400_BAD_REQUEST)


class StudentUpdateAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def put(self, request, pk):
        response_holder = {}

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

        def callback(result): response_holder.update(result)

        book_all_show_requested.send(sender=self.__class__, callback=callback)
        return Response(
            response_holder,
            status=status.HTTP_200_OK if response_holder.get("success") else status.HTTP_400_BAD_REQUEST)


class BookAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, pk):
        response_holder = {}

        def callback(result): response_holder.update(result)

        book_show_requested.send(sender=self.__class__, callback=callback, pk=pk)
        return Response(response_holder,
                        status=status.HTTP_200_OK if response_holder.get("success") else status.HTTP_400_BAD_REQUEST)


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
