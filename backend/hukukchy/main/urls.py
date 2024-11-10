from django.urls import path
from . import views

urlpatterns = [
    path('service_categories/',views.ServiceCategoryListView.as_view()),
    path('service_categories/<int:pk>',views.ServiceCategoryDetailView.as_view()),
    path('book_upload/',views.BookUpload.as_view()),
    path('book_detail/<int:pk>',views.BookDetail.as_view()),
    path('get_books_by_category/<int:category_id>',views.GetBooksByCategory.as_view()),
    path('news_category_list/',views.NewsCategoryListView.as_view()),
    path('news_category_detail/<int:pk>',views.NewsCategoryDetailView.as_view()),
    path('news_listview/',views.NewsListView.as_view()),
    path('news_detail/<int:pk>',views.NewsDetailView.as_view()),
]
