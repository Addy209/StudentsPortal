from rest_framework import serializers
from rest_framework import fields
from rest_framework import validators
from rest_framework.exceptions import ValidationError
from .models import *
from django.contrib.auth.models import User
import re

class UserSignup(serializers.ModelSerializer):
    def validate(self,data):
        valid=re.search("^[a-zA-Z][a-zA-Z0-9._]{3,9}$",data["username"])
        if valid:
            return data
        else:
            raise ValidationError("Username not in required format")

    class Meta():
        model=User
        fields=["username","password","first_name","last_name"]

class StudentSignup(serializers.ModelSerializer):
    class Meta():
        model=Student
        exclude=["user"]

class StudentLogin(serializers.Serializer):
    username=serializers.RegexField("^[a-zA-Z][a-zA-Z0-9._]{3,9}$")
    password=serializers.CharField()