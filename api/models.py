from django.db import models
from django.contrib.auth.models import User

STATUS_CHOICES = (
    ('publish','Publish'),
    ('draft', 'Draft'),
    ('edit', 'Edit'),
    
)
class Category(models.Model):
    """each post will have category"""
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.name
    
class Post(models.Model):
    """post table"""
    title = models.CharField(max_length=255)
    blog_url = models.CharField(max_length=255, db_index=True,unique=True)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    category = models.ManyToManyField(Category,related_name='post_comments')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='author_blogs')
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')
    def __str__(self):
        return self.title
    
class Comment(models.Model):
    """comments on post"""
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='post_comments')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_comments')
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ['-created_at']#Latest comments first

    def __str__(self):
        return f'Comment by {self.user.username} on {self.post.title}'


