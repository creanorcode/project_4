# Import necessary modules
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from django.http import JsonResponse
from django.views.decorators.http import require_POST, require_http_methods
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
import json
from .models import Post, Comment, Category
from .forms import PostForm, CommentForm

# View for listing all posts (homepage)
def post_list(request):
    # Retrieve posts ordered by creation date (newest first)
    posts = Post.objects.all().order_by('-created_at')
    return render(request, 'post/post_list.html', {'posts': posts})

# View for displaying post details along with its comments
def post_detail(request, pk):
    # Get the specific post or return 404 if not found
    post = get_object_or_404(Post, pk=pk)
    # Retrieve comments related to the post ordered by creation date
    comments = post.comments.all().order_by('created_at')
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user
            comment.post = post
            comment.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = CommentForm()
    return render(request, 'posts/post_detail.html', {'post': post, 'comments': comments, 'form': form})

# View for creating a new post
@login_required
def post_create(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'posts/post_form.html', {'form': form})

# View for updating an existing post
@login_required
def post_update(request, pk):
    post = get_object_or_404(Post, pk=pk)
    # Ensure only the post author or staff can update the post
    if request.user != post.author and not request.user.is_staff:
        return render(request, 'posts/error.html', {'message': 'You are not authorized to edit this post.'})
    
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'posts/post_form.html', {'form': form})

# View for deleting a post
def post_delete(request, pk):
    post = get_object_or_404(Post, pk=pk)
    # Ensure only the post suthor or staff can delete the post
    if request.user != post.author and not request.user.is_staff:
        return render(request, 'posts/error.html', {'message': 'You are not authorized to delete this post.'})
    
    if request.method == "POST":
        post.delete()
        return redirect('post_list')
    return render(request, 'posts/post_confirm_delete.html', {'post': post})

# View for updating a comment
@login_required
def comment_update(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    # Only allow the comment´s author or staff to update it
    if request.user != comment.author and not request.user.is_staff:
        return render(request, 'posts/error.html', {'message': 'You are not authorized to edit this comment.'})
    
    if request.method == "POST":
        form = CommentForm(request.POST, instance=comment)
        if form.is_valid():
            form.save()
            return redirect('post_detail', pk=comment.post.pk)
    else:
        form = CommentForm(instance=comment)
    return render(request, 'posts/comment_form.html', {'form': form, 'comment': comment})

# View for deleting a comment
@login_required
def comment_delete(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    # Only allow the comment´s author or staff to delete it
    if request.user != comment.author and not request.user.is_staff:
        return render(request, 'posts/error.html', {'message': 'You are not authorized to delete this comment.'})
    
    if request.method == "POST":
        post_pk = comment.post.pk
        comment.delete()
        return redirect('post_detail', pk=post_pk)
    return render(request, 'posts/comment_confirm_delete.html', {'comment': comment})
