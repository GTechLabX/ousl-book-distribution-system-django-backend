from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from .serializers.register_serializer import *


class LoginAPIView(APIView):
    def post(self, request):
        # get username and password from the request
        username = request.data.get('username')
        password = request.data.get('password')

        # check whether username and password available or not
        if not username or not password:
            return Response({'error': 'Username and Password are required!'}, status=status.HTTP_400_BAD_REQUEST)

        user = authenticate(username=username, password=password)

        # if user is available then issue refresh and access token else send an error message
        if user:
            refresh = RefreshToken.for_user(user)
            return Response(
                {
                    'refresh': str(refresh),
                    'access': str(refresh.access_token),
                    'username': user.username,
                }
            )
        else:
            return Response({
                'error': 'Invalid Credentials',
            },
                status=status.HTTP_401_UNAUTHORIZED
            )


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


class StudentRegAPIView(APIView):
    pass