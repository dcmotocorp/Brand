from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import UserRegistrationSerializer, UserLoginSerializer
from django.contrib.auth import authenticate, login
from .models import User




from django.contrib.auth.views import PasswordResetView
from django.urls import reverse_lazy
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

class UserRegistrationView(APIView):
    def post(self, request):
        serializer = UserRegistrationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserLoginView(APIView):
    def post(self, request):
        print("===================w")
        serializer = UserLoginSerializer(data=request.data)
        print("===================w")
        if serializer.is_valid():
            print("===================w")
            username = serializer.validated_data['username']
            password = serializer.validated_data['password']
            print("===================================================")
            print(username)
            print(password)

            if '@' in username:
                user1 = User.objects.filter(email=username).first()
                user = authenticate(request, username=user1.username, password=password)
            else:
                user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
                return Response({'message': 'Login successful'})
            else:
                return Response({'message': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)






class CustomPasswordResetView(PasswordResetView):
    def get_success_response(self):
        return Response(
            {'detail': 'Password reset email sent.'},
            status=status.HTTP_200_OK
        )

class PasswordResetAPIView(APIView):
    def post(self, request):
        email = request.data.get('email')
        if not email:
            return Response(
                {'detail': 'Please provide an email address.'},
                status=status.HTTP_400_BAD_REQUEST
            )
        view = CustomPasswordResetView.as_view()
        return view(request._request).render()