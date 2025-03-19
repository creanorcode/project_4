# posts/tests.py

from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Post, Category, Comment

# Test case for the Post model
class PostModelTest(TestCase):
    def setUp(self):
        # Create a test user and a category for the post
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.category = Category.objects.create(name='News')
        self.post = Post.objects.create(
            title='Test Post',
            content='This is test content for the post.',
            author= self.user,
            category=self.category
        )

    def test_vote_score(self):
        # Set up votes and verify the vote score is calculated correctly
        self.post.upvotes = 5
        self.post.downvotes = 2
        self.assertEqual(self.post.vote_score(), 3)

# Test case for post list view functionality
class PostViewTest(TestCase):
    def setUp(self):
        # Create a test user, category and a post
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.category = Category.objects.create(name='News')
        self.post = Post.objects.create(
            title='Test Post',
            content='This is test content for the post.',
            author=self.user,
            category=self.category
        )

    def test_post_list_view(self):
        # Retrieve the post list page and check if the post is displayed
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test Post')
