from . import models
from rest_framework import serializers

class ServiceCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model=models.ServiceCategory
        fields='__all__'

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model=models.BookUpload
        fields='__all__'
    
class NewsCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model=models.NewsCategory
        fields='__all__'

class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model=models.News
        fields='__all__'
        
