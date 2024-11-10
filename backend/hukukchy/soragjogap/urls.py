from django.urls import path
from . import views

urlpatterns = [
    path('questions/',views.QuestionListCreateAPIView.as_view()),
    path('questions/<int:pk>', views.QuestionDetailAPIView.as_view()), 
]
