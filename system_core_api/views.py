from django.contrib.auth.decorators import login_required
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from events.signals import *


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
    authentication_classes = [IsAuthenticated]

    def put(self, request, pk):
        response_holder = {}

        def callback(result):
            response_holder.update(result)

        student_update_requested.send(
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


class AllStudentAPIView(APIView):
    def get(self, request):
        response_holder = {}

        def callback(result):
            response_holder.update(result)

        student_all_requested.send(
            sender=self.__class__,
            data=request,
            callback=callback,
        )

        # send back to the user whatever dispatch system send
        if response_holder.get("success"):
            return Response(response_holder, status=status.HTTP_200_OK)
        else:
            return Response(response_holder, status=status.HTTP_400_BAD_REQUEST)


class StudentAPIView(APIView):
    authentication_classes = [IsAuthenticated]

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
