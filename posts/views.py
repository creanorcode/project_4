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
