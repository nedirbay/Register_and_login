from django.shortcuts import render
from rest_framework import generics
from . import serializers
from . import models

class ServiceCategoryListView(generics.ListCreateAPIView):
    queryset = models.ServiceCategory.objects.all()
    serializer_class = serializers.ServiceCategorySerializer

class ServiceCategoryDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.ServiceCategory.objects.all()
    serializer_class = serializers.ServiceCategorySerializer

class BookUpload(generics.ListCreateAPIView):
    queryset = models.BookUpload.objects.all()
    serializer_class = serializers.BookSerializer

class GetBooksByCategory(generics.ListCreateAPIView):
    serializer_class = serializers.BookSerializer
    
    def get_queryset(self):
        category_id = self.kwargs['category_id']
        return models.BookUpload.objects.filter(category_id=category_id)

class BookDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.BookUpload.objects.all()
    serializer_class = serializers.BookSerializer

class NewsCategoryListView(generics.ListCreateAPIView):
    queryset = models.NewsCategory.objects.all()
    serializer_class = serializers.NewsCategorySerializer

class NewsCategoryDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.NewsCategory.objects.all()
    serializer_class=serializers.NewsCategorySerializer

class NewsListView(generics.ListCreateAPIView):
    queryset = models.News.objects.all()
    serializer_class = serializers.NewsSerializer

class NewsDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.News.objects.all()
    serializer_class = serializers.NewsSerializer

    
