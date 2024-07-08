# workspace/models.py
from django.conf import settings
from django.db import models

class Post(models.Model):
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='leisure_posts')  # 使用 settings.AUTH_USER_MODEL
    image = models.ImageField(upload_to='post_images/', blank=True, null=True)

    def __str__(self):
        return f"{self.author.username}: {self.created_at}"  # 确保使用 username 或其他字段替代 name

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='comments')  # 使用 settings.AUTH_USER_MODEL
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.author.username} - {self.post.id}"  # 确保使用 username 或其他字段替代 name

class Reaction(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='reactions')
    reactor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='reactions')  # 使用 settings.AUTH_USER_MODEL
    emoji = models.CharField(max_length=10)

    def __str__(self):
        return f"{self.reactor.username} reacted with {self.emoji}"  # 确保使用 username 或其他字段替代 name

class Vote(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='votes')
    voter = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='votes')  # 使用 settings.AUTH_USER_MODEL
    vote_type = models.CharField(max_length=10, choices=[('up', 'Upvote'), ('down', 'Downvote')])

    def __str__(self):
        return f"{self.voter.username} - {self.vote_type}"  # 确保使用 username 或其他字段替代 name

class Poll(models.Model):
    question = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.question

class Option(models.Model):
    poll = models.ForeignKey(Poll, on_delete=models.CASCADE, related_name='options')
    text = models.CharField(max_length=100)
    votes = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='option_votes')  # 使用 settings.AUTH_USER_MODEL

    def __str__(self):
        return self.text
