from django.contrib import admin
from .models import Post, Comment, Reaction, Vote, Poll, Option


admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Reaction)
admin.site.register(Vote)
admin.site.register(Poll)
admin.site.register(Option)
