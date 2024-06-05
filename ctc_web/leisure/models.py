from django.db import models

# Create your models here.

from django.db import models

class Member(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return self.name

class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(Member, on_delete=models.CASCADE, related_name='posts')

    def __str__(self):
        return self.title

class Vote(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='votes')
    voter = models.ForeignKey(Member, on_delete=models.CASCADE, related_name='votes')
    vote_type = models.CharField(max_length=10, choices=[('up', 'Upvote'), ('down', 'Downvote')])

    def __str__(self):
        return f"{self.voter.name} - {self.vote_type}"
