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

# View for handling post voting via AJAX
@require_POST
@login_required
def vote_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    data = json.loads(request.body)
    vote = data.get('vote')
    # Increment upvotes or downvotes based on vote type
    if vote == 'up':
        post.upvotes += 1
    elif vote == 'down':
        post.downvotes += 1
    post.save()
    return JsonResponse({'vote_score': post.vote_score()})

# API view for updating a post (example using PUT method)
@require_http_methods(["PUT"])
@login_required
def api_post_update(request, pk):
    post = get_object_or_404(Post, pk=pk)
    # Only allow post author or staff to update the post
    if request.user != post.author and not request.user.is_staff:
        return JsonResponse({'error': 'Not authorized'}, status=403)
    
    data = json.loads(request.body)
    form = PostForm(data, instance=post)
    if form.is_valid():
        form.save()
        return JsonResponse({'message': 'Post updated', 'vote_score': post.vote_score()})
    return JsonResponse(form.errors, status=400)

# View for user registration using Django´s UserCreationForm
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('post_list')
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})

# View for displaying a user´s profile and their posts
@login_required
def user_profile(request, username):
    from django.contrib.auth.models import User
    user_profile = get_object_or_404(User, username=username)
    user_posts = Post.objects.filter(author=user_profile).order_by('-created_at')
    return render(request, 'posts/user_profile.html', {'user_profile': user_profile, 'user_posts': user_posts})

# Optional: Class-based views for updating a post uding mixins
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import UpdateView

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'posts/post_form.html'

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author or self.request.user.is_staff

# Custom admin views for user management (outside of Django admin)
@user_passes_test(lambda u: u.is_staff)
def manage_users(request):
    from django.contrib.auth.models import User
    users = User.objects.all().order_by('username')
    return render(request, 'posts/manage_users.html', {'users': users})

@user_passes_test(lambda u: u.is_staff)
def lock_user(request, user_id):
    from django.contrib.auth.models import User
    user = User.objects.get(id=user_id)
    user.is_active = False
    user.save()
    messages.success(request, f"User {user.username} has been locked.")
    return redirect('manage_users')

@user_passes_test(lambda u: u.is_staff)
def delete_user(request, user_id):
    from django.contrib.auth.models import User
    user = User.objects.get(id=user_id)
    user.delete()
    messages.success(request, f"User {user.username} has been deleted.")
    return redirect('manage_users')
