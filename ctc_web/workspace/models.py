from django.db import models
from django.contrib.auth.models import User

class Staff(models.Model):
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    email = models.EmailField()
    user = models.OneToOneField(User, on_delete=models.CASCADE)  # 添加 user 字段以关联 User 模型

    def __str__(self):
        return self.name

class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()
    staff = models.ForeignKey(Staff, on_delete=models.CASCADE, related_name='projects')

    def __str__(self):
        return self.title

class Post(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='posts')
    title = models.CharField(max_length=200)
    content = models.TextField()
    image = models.ImageField(upload_to='post_images/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts',default=1)  # 添加 author 字段

    def __str__(self):
        return self.title
