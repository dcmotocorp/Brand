from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import UserRegistrationSerializer, UserLoginSerializer
from django.contrib.auth import authenticate, login
from .models import User
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from django.contrib.auth.views import PasswordResetView
from django.urls import reverse_lazy
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.core.mail import send_mail
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.conf import settings
from rest_framework.decorators import api_view

class UserRegistrationView(APIView):
    def post(self, request):
        serializer = UserRegistrationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserLoginView(APIView):
    authentication_classes = [BasicAuthentication]
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


def send_email_view(subject,message,from_email,recipient_list):
    subject = 'Hello from BigBazz!'
    message = 'This is a test email sent using Django.'
    from_email = 'your_email@gmail.com'  # Replace this with your email address
    recipient_list = ['recipient@example.com']  # Replace this with the recipient's email address

    send_mail(subject, message, from_email, recipient_list)

@api_view(['POST'])
def reset_username(request):
    email = request.POST.get('email')
    user_data = User.objects.filter(email=email).first()
    if not user_data:
        return Response({'Error':'This Email is Not Register'},status=status.HTTP_400_BAD_REQUEST)
    subject = "Your Username"
    message = f"your username for your account is : {user_data.username}"
    from_mail  = settings.EMAIL_HOST_USER
    to_mail  = [user_data.email]
    try:
        send_email_view(subject,message,from_mail,to_mail)
    except Exception as ex:
        print("failed to send mail")
    return Response({'success':"Email send for reset username"},status=status.HTTP_200_OK) 
