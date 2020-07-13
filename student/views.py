from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import *
from rest_framework.authtoken.models import Token
from django.shortcuts import get_object_or_404
from django.contrib.auth import authenticate

class SignUpView(APIView):
    def post(self,request):
        user_serializer=UserSignup(data=request.data)
        student_serilizer=StudentSignup(data=request.data)
        if user_serializer.is_valid() and student_serilizer.is_valid():
            user=user_serializer.save()
            user.set_password(user.password)
            user.save()

            student_serilizer.save(user=user)
            token,created=Token.objects.get_or_create(user=user)
            return Response({"token":token.key})
        else:
            return Response(status=404)

class LoginView(APIView):
    def post(self, request):
        login_serializer=StudentLogin(data=request.data)
        if login_serializer.is_valid():
            username=login_serializer.validated_data["username"]
            password=login_serializer.validated_data["password"]
            user=authenticate(username=username,password=password)
            if user and user.is_active:
                token=Token.objects.get(user=user)
                return Response({"token":token.key})
            else:
                return Response(status=404)
        else:
            return Response(status=401)

