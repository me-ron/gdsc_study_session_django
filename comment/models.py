from django.db import models

# Create your models here.

class Comment(models.Model):
    content = models.TextField()
    created_time = models.DateTimeField(auto_now_add=True)
    modified_time = models.DateTimeField(auto_now=True)

