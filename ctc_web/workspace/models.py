# workspace/models.py
from django.conf import settings
from django.db import models

class Post(models.Model):
    project = models.ForeignKey('Project', on_delete=models.CASCADE, related_name='workspace_posts')
    title = models.CharField(max_length=200)
    content = models.TextField()
    image = models.ImageField(upload_to='post_images/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='posts')  # 使用 settings.AUTH_USER_MODEL

    def __str__(self):
        return self.title

class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()
    manager = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='managed_projects')  # 使用 settings.AUTH_USER_MODEL

    def __str__(self):
        return self.title
