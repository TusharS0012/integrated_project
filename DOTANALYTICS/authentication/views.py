from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth import authenticate
from .serilizer import RegisterSerializer, LoginSerializer
from rest_framework.authtoken.models import Token
from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponseRedirect
from rest_framework.views import APIView
 
from django.core.mail import send_mail
from django.contrib.auth.models import User
import random
 
from .models import PasswordResetOTP
 


User = get_user_model()

class RegisterView(APIView):
     
    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return render(request,'index.html' )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LoginView(APIView):
    def post(self, request):
        serializer = LoginSerializer(data=request.data)

        if serializer.is_valid():
            email = serializer.validated_data['email']
            password = serializer.validated_data['password']

            try:
                user = User.objects.get(email=email)
            except User.DoesNotExist:
                return Response({"error": "Invalid email or password"}, status=status.HTTP_400_BAD_REQUEST)

            # Authenticate user
            user = authenticate(username=user.email, password=password)
            if user is not None:
                # Generate or retrieve the token
                token, created = Token.objects.get_or_create(user=user)
                
                # Redirect to React app with token and user details as query parameters
                response_data = {
                "token": token.key,
                "redirect_url": f'http://localhost:5173/login-redirect?token={token.key}&email={user.email}&first_name={user.first_name}&last_name={user.last_name}'
                }
                return Response(response_data, status=status.HTTP_200_OK)
            else:
                return Response({"error": "Invalid email or password"}, status=status.HTTP_400_BAD_REQUEST)
        
        # If serializer validation fails
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

     

def home (request):
    return render(request, "index.html")


def saas_view(request):
    return render(request, 'saas.html')


def cyber_view(request):
    return render(request, 'cyber.html')

def docker_view(request):
    return render(request, 'docker.html')

def ArtficialIntelligence_view(request):
    return render(request, 'AI.html')

def python_view(request):
    return render(request, 'python.html')

def MachineLearning_view(request):
    return render(request, 'ML.html')

 


class RequestOTPView(APIView):
    def post(self, request):
        email = request.data.get("email")
        try:
            user = User.objects.get(email=email)
            otp = random.randint(100000, 999999)
            user.profile.otp = otp  # Assuming `otp` field exists in the User profile model.
            user.profile.save()
            send_mail(
                "Your OTP for Password Reset",
                f"Your OTP is {otp}. It is valid for 10 minutes.",
                "from@example.com",
                [email],
            )
            return Response({"message": "OTP sent to your email."}, status=status.HTTP_200_OK)
        except User.DoesNotExist:
            return Response({"error": "User with this email does not exist."}, status=status.HTTP_404_NOT_FOUND)
 
 
 
from .models import PasswordResetOTP

class ValidateOTPAndResetPasswordView(APIView):
    def post(self, request):
        email = request.data.get("email")
        otp = request.data.get("otp")
        new_password = request.data.get("new_password")
        confirm_password = request.data.get("confirm_password")

        if new_password != confirm_password:
            return Response({"error": "Passwords do not match."}, status=status.HTTP_400_BAD_REQUEST)

        try:
            otp_record = PasswordResetOTP.objects.filter(user__email=email, otp=otp).last()

            if otp_record and otp_record.is_otp_valid():
                user = otp_record.user
                user.set_password(new_password)
                user.save()
                otp_record.delete()  # Clean up the OTP after successful reset
                return Response({"message": "Password reset successfully."}, status=status.HTTP_200_OK)
            else:
                return Response({"error": "Invalid or expired OTP."}, status=status.HTTP_400_BAD_REQUEST)

        except User.DoesNotExist:
            return Response({"error": "User with this email does not exist."}, status=status.HTTP_404_NOT_FOUND)
