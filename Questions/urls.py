from django.contrib import admin
from django.urls import path,include
from .views import *
urlpatterns = [
    path("classinfo/", ClassInfoView.as_view()),
    path("questions/<int:id>", QuestionAnswerView.as_view()),
    path("questions/", QuestionAnswerView.as_view()),
    
]