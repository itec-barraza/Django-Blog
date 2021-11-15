from django.urls import path
from . import views

urlpatterns = [
    path('', views.blog, name='blog'),
    path('category/<int:category_id>', views.category, name="category"),
    path('user/<int:user_id>', views.user, name="user"),
    path('addPost/', views.addPost, name="addPost")
]
