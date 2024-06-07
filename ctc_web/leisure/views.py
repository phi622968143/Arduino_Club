from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.db import models
from .models import Member, Post, Comment, Reaction, Poll, Option
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required
from django.contrib import messages

@login_required
def post_list(request):
    posts = Post.objects.all()
    polls = Poll.objects.order_by('-created_at')[:5]  # 获取最新的五个投票

    reactions_count = {}
    for post in posts:
        reactions = post.reactions.values('emoji').annotate(count=models.Count('emoji'))
        reactions_count[post.id] = {reaction['emoji']: reaction['count'] for reaction in reactions}
    
    return render(request, 'l_post.html', {'posts': posts, 'polls': polls, 'reactions_count': reactions_count})

@csrf_exempt
@require_POST
@login_required
def post_action(request):
    action_type = request.POST.get('action_type')

    if action_type == 'create_post':
        content = request.POST['content']
        image = request.FILES.get('image')
        author = Member.objects.get(id=request.user.id)  # 假设用户已登录
        Post.objects.create(content=content, author=author, image=image)

    elif action_type == 'add_comment':
        post_id = request.POST['post_id']
        post = get_object_or_404(Post, id=post_id)
        content = request.POST['content']
        author = Member.objects.get(id=request.user.id)
        Comment.objects.create(post=post, author=author, content=content)

    elif action_type == 'add_reaction':
        post_id = request.POST['post_id']
        post = get_object_or_404(Post, id=post_id)
        emoji = request.POST['emoji']
        reactor = Member.objects.get(id=request.user.id)
        Reaction.objects.create(post=post, reactor=reactor, emoji=emoji)
        reaction_count = post.reactions.filter(emoji=emoji).count()
        return JsonResponse({'success': True, 'emoji': emoji, 'count': reaction_count})

    elif action_type == 'create_poll':
        question = request.POST['question']
        option1 = request.POST['option1']
        option2 = request.POST['option2']
        poll = Poll.objects.create(question=question)
        Option.objects.create(poll=poll, text=option1)
        Option.objects.create(poll=poll, text=option2)

    elif action_type == 'vote':
        poll_id = request.POST['poll_id']
        poll = get_object_or_404(Poll, id=poll_id)
        option_id = request.POST['option_id']
        option = get_object_or_404(Option, id=option_id)
        voter = Member.objects.get(id=request.user.id)
        option.votes.add(voter)

    elif action_type == 'delete_post':
        post_id = request.POST['post_id']
        post = get_object_or_404(Post, id=post_id)
        if request.user == post.author:
            post.delete()
            messages.success(request, '文章已删除')
        else:
            messages.error(request, '您没有权限删除这篇文章')

    elif action_type == 'delete_poll':
        poll_id = request.POST['poll_id']
        poll = get_object_or_404(Poll, id=poll_id)
        poll.delete()

    return redirect('post_list')
