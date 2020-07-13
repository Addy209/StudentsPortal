from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Student(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE)
    age=models.IntegerField()
    city=models.CharField(max_length=30)
    grade=models.CharField(max_length=10)
    board=models.CharField(max_length=10)

    def __str__(self) -> str:
        return (self.user.first_name+" "+self.user.last_name)
