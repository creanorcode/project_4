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

# Routes for updating and deleting posts

# Route for updating an existing post; optionally, you can use a class-based view instead
path('post/<int:pk>/edit/', views.post_update, name='post_update'),
# Route for deleting a post
path('post/<int:pk>/delete/', views.post_delete, name='post_delete'),

# Routes for post voting and comment management

# Route for voting on a post via AJAX
path('post/<int:pk>/vote/', views.vote_post, name='vote_post'),

# Routes for editing and deleting comments
path('comment/<int:pk>/edit/', views.comment_update, name='comment_update'),
path('comment/<int:pk>/delete/', views.comment_delete, name='comment_delete'),

# Route for viewing a user´s profile by username
path('user/<str:username>/', views.user_profile, name='user_profile'),

# API endpoint example for updating a post via PUT
path('api/post/<int:pk>/update/', views.api_post_update, name='api_post_update'),
