# posts/urls.py

from django.urls import path
from . import views

# Basic post routes for listing, detail view and creation
urlpatterns [
    # Route for homepage (post list)
    path('', views.post_list, name='post_list'),
    # Route to view details of a specific post by primary key
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    # Route for creating a new post
    path('post/new/', views.post_create, name='post_create'),
]
