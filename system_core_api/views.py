from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken


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
        username = request.data.get('username')
        password = request.data.get('password')
        first_name = request.data.get('first_name')
        last_name = request.data.get('last_name')
        email = request.data.get('email')

        
