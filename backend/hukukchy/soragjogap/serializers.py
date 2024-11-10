from rest_framework import serializers
from .models import Question,KanunUpload

class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = '__all__'


