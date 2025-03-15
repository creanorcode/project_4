from django.db import models
from django.contrib.auth.models import User

# Category nodel for organizing posts by topic.
class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

# Post model representing individual posts with title, content, and vote tracking.
class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
    upvotes = models.IntegerField(default=0)
    downvotes = models.IntegerField(default=0)

    def __str__(self):
        return self.title
    
    def vote_score(self):
        return self.upvotes - self.downvotes

