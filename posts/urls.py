# posts/urls.py

from django.urls import path, include
from . import views
from django.contrib import admin
from .views import profile, edit_profile

# Basic post routes for listing, detail view and creation
urlpatterns = [
    # Route for homepage (post list)
    path('', views.post_list, name='post_list'),
    # Route to view details of a specific post by primary key
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    # Route for creating a new post
    path('post/new/', views.post_create, name='post_create'),
    # Route for accounts, django-allauth
    path('accounts/', include('allauth.urls')),

    # Routes for updating and deleting posts

    # Route for updating an existing post; optionally,
    # you can use a class-based view instead
    path('post/<int:pk>/edit/', views.post_update, name='post_update'),
    # Route for deleting a post
    path('post/<int:pk>/delete/', views.post_delete, name='post_delete'),

    # Routes for post voting and comment management

    # Route for voting on a post via AJAX
    path('post/<int:pk>/vote/', views.vote_post, name='vote_post'),

    # Routes for editing and deleting comments
    path('comment/<int:pk>/edit/', views.comment_update,
         name='comment_update'),
    path('comment/<int:pk>/delete/', views.comment_delete,
         name='comment_delete'),

    # Route for viewing your own profile without slug
    path('profile/', views.profile, name='my_profile'),
    # Route for viewing a user´s profile by usernamn
    path('user/<str:username>/', views.profile, name='profile'),

    path('profile/', profile, name='my_profile'),
    path('profile/edit/', edit_profile, name='edit_profile'),
    path('profile/<str:username>/', profile, name='profile'),

    # API endpoint example for updating a post via PUT
    path('api/post/<int:pk>/update/', views.api_post_update,
         name='api_post_update'),

    # Custom admin routes for managing user accounts

    # Route for managing users (custom admin page)
    path('admin/manage-users/', views.manage_users, name='manage_users'),
    # Route for locking a user account
    path('admin/lock-user/<int:user_id>/', views.lock_user, name='lock_user'),
    # Route for deleting a user account
    path('admin/delete-user/<int:user_id>/', views.delete_user,
         name='delete_user'),
]
