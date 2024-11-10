from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import Question
from . import serializers
from rest_framework.response import Response 
from rest_framework import status
from . import models


class QuestionListCreateAPIView(generics.ListCreateAPIView):
    queryset = Question.objects.all()
    serializer_class = serializers.QuestionSerializer


class QuestionDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Question.objects.all()
    serializer_class = serializers.QuestionSerializer



