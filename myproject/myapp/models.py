# Create your models here.
from django.db import models
from django.contrib.auth.models import User # import User model để định nghĩa

class Post(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE) # Yêu cầu chỉ định User làm author của blog
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)