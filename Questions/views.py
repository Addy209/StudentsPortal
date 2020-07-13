from django.shortcuts import get_list_or_404,get_object_or_404
from rest_framework import viewsets,mixins
from .serializers import *
from .models import *
from rest_framework.views import APIView
from django.contrib.auth.models import User
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.authentication import TokenAuthentication
from django.contrib.auth import authenticate
from rest_framework.response import  Response
from rest_framework.authtoken.models import Token


# Create your views here.
class ClassInfoView(APIView):
    queryset=AllClasses.objects.all()
    permission_classes=[IsAuthenticated]
    authentication_classes=[TokenAuthentication]
    def get(self, request):
        classpks=get_list_or_404(ClassInfo,user=request.user)
        print(classpks[0].classname)
        course=[]
        for i in range(len(classpks)):
            course.append(get_object_or_404(self.queryset, pk=classpks[i].id))   
        print(course)
        class_ser=ClassInfoSerializer(course, many=True)
        return Response({"classes":class_ser.data})

class QuestionAnswerView(APIView):
    queryset1=Questions.objects.all()
    queryset2=Answer.objects.all()
    permission_classes=[IsAuthenticated]
    authentication_classes=[TokenAuthentication]
    def getEl(self,obj):
        qa={}
        qa["qaid"]=obj.id
        qa["question"]=get_object_or_404(self.queryset1,pk=obj.question.id).question
        if obj.answer:
            qa["answer"]=get_object_or_404(self.queryset2,pk=obj.answer.id).answer
        else:
            qa["answer"]=None
        
        print(qa)
        return qa

    def get(self, request):
        pks=get_list_or_404(QuestionAndAnswers,user=request.user)
        QA=map(self.getEl,pks)
        serializers=QuestionSerializer(QA, many=True)
        return Response({"value":serializers.data})
    
    def put(self, request, id):
        answer=AnswerSerializer(data=request.data)
        ans=""
        if answer.is_valid():
            ans=answer.save()
        qaser=QuestionAndAnswersSerializers(self.get_Object(id),data={"answer":ans.id},partial=True)
        if qaser.is_valid():
            qaser.save()
        return Response({"val":qaser.data},status=200)

    def get_Object(self,id):
        return get_object_or_404(QuestionAndAnswers,pk=id)
        
