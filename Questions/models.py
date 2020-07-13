from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class AllClasses(models.Model):
    class_name=models.CharField(max_length=20)
    class_desc=models.TextField()
    start_time=models.TimeField()
    duration=models.IntegerField()

    
    def __str__(self) -> str:
        return self.class_name

class ClassInfo(models.Model):
    user=models.ForeignKey(User, on_delete=models.PROTECT)
    classname=models.ForeignKey(AllClasses,on_delete=models.PROTECT)

    def __str__(self) -> str:
        return self.classname.class_name


class Questions(models.Model):
    question=models.TextField()
    def __str__(self) -> str:
        return self.question

class Answer(models.Model):
    answer=models.TextField()
    def __str__(self) -> str:
        return self.answer

class QuestionAndAnswers(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    question=models.ForeignKey(Questions, on_delete=models.CASCADE)
    answer=models.ForeignKey(Answer,null=True,blank=True,on_delete=models.CASCADE)
    
    def __str__(self) -> str:
        return "{} {}".format(self.user.get_full_name(),self.question)
