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

 
 