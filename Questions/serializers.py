from rest_framework import serializers
from rest_framework import fields
from .models import *

class ClassInfoSerializer(serializers.ModelSerializer):
    class Meta():
        model=AllClasses
        fields="__all__"

class AnswerSerializer(serializers.ModelSerializer):
    class Meta():
        model=Answer
        fields=["id","answer"]

class QuestionSerializer(serializers.Serializer): 
    qaid=serializers.IntegerField()
    question=serializers.CharField()
    answer=serializers.CharField()
    
    

class QuestionAndAnswersSerializers(serializers.ModelSerializer):
    class Meta():
        model=QuestionAndAnswers
        fields="__all__"
