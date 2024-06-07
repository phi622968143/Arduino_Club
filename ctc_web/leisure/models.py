from django.db import models

class Member(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return self.name

class Post(models.Model):
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(Member, on_delete=models.CASCADE, related_name='posts')
    image = models.ImageField(upload_to='post_images/', blank=True, null=True)

    def __str__(self):
         return f"{self.author.name}: {self.created_at}"

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(Member, on_delete=models.CASCADE, related_name='comments')
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.author.name}+{self.post.id}"

class Reaction(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='reactions')
    reactor = models.ForeignKey(Member, on_delete=models.CASCADE, related_name='reactions')
    emoji = models.CharField(max_length=10)

    def __str__(self):
        return f"{self.reactor.name} reacted with {self.emoji}"

class Vote(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='votes')
    voter = models.ForeignKey(Member, on_delete=models.CASCADE, related_name='votes')
    vote_type = models.CharField(max_length=10, choices=[('up', 'Upvote'), ('down', 'Downvote')])

    def __str__(self):
        return f"{self.voter.name} - {self.vote_type}"

class Poll(models.Model):
    question = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.question

class Option(models.Model):
    poll = models.ForeignKey(Poll, on_delete=models.CASCADE, related_name='options')
    text = models.CharField(max_length=100)
    votes = models.ManyToManyField(Member, related_name='option_votes')

    def __str__(self):
        return self.text
