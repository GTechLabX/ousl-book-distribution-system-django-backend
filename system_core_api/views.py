from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from auth_sys.serializers.register_serializer import *
from events.signals import *





class RegisterAPIView(APIView):
    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                'message': 'User has been successfully register'
            }, status=status.HTTP_201_CREATED)

        else:
            return Response({
                'error': serializer.errors
            }, status=status.HTTP_400_BAD_REQUEST)


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
        # return whatever the dispatch system send back

        if response_holder.get("success"):
            return Response(response_holder, status=status.HTTP_201_CREATED)
        else:
            return Response(response_holder, status=status.HTTP_400_BAD_REQUEST)


class StudentRegAPIView(APIView):
    # authentication_classes = [authentication.SessionAuthentication, authentication.TokenAuthentication]
    # permission_classes = [permissions.IsAuthenticated]

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
