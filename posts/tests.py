# posts/tests.py

from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Post, Category, Comment


# Test case for the Post model
class PostModelTest(TestCase):
    def setUp(self):
        # Create a test user and a category for the post
        self.user = User.objects.create_user(username='testuser',
                                             password='12345')
        self.category = Category.objects.create(name='News')
        self.post = Post.objects.create(
            title='Test Post',
            content='This is test content for the post.',
            author=self.user,
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
        self.user = User.objects.create_user(username='testuser',
                                             password='12345')
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


# Test case for updating and deleting posts
class PostCRUDTest(TestCase):
    def setUp(self):
        # Create a test user, category and a post to test CRUD operations
        self.user = User.objects.create_user(username='testuser',
                                             password='12345')
        self.category = Category.objects.create(name='News')
        self.post = Post.objects.create(
            title='Test User',
            content='Initial test content.',
            author=self.user,
            category=self.category
        )

    def test_update_post(self):
        # Login the test user
        self.client.login(username='testuser', password='12345')
        # Get the URL for updating the post and send new data via POST
        url = reverse('post_update', kwargs={'pk': self.post.pk})
        response = self.client.post(url, {
            'title': 'Updated Post',
            'content': 'Updated content for the post.',
            'category': self.category.pk
        })
        # Expect a redirect after update (status code 302)
        self.assertEqual(response.status_code, 302)
        self.post.refresh_from_db()
        # Verify that the post title has been updated
        self.assertEqual(self.post.title, 'Updated Post')

    def test_delete_post(self):
        # Login the test user
        self.client.login(username='testuser', password='12345')
        # Get the URL for deleting the post and send a POST request
        url = reverse('post_delete', kwargs={'pk': self.post.pk})
        response = self.client.post(url)
        # Expect a redirect after deletion (status code 302)
        self.assertEqual(response.status_code, 302)
        # Verify that the post no longer exists in the database
        self.assertFalse(Post.objects.filter(pk=self.post.pk).exists())
