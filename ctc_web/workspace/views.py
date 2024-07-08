from django.shortcuts import render, get_object_or_404, redirect
from .models import Project, Post
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from user.models import User
@login_required
def project_list(request):
    """展示项目列表，允许创建新项目"""
    projects = Project.objects.all()

    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        start_date = request.POST.get('start_date')
        end_date = request.POST.get('end_date')

        if title and description and start_date and end_date:
            Project.objects.create(
                title=title,
                description=description,
                start_date=start_date,
                end_date=end_date,
                manager=request.user  # 将当前用户设为项目经理
            )
            messages.success(request, '项目已创建')
            return redirect('project_list')
        else:
            messages.error(request, '请填写所有必填字段')

    context = {
        'projects': projects,
    }
    return render(request, 'project_list.html', context)

@login_required
def post_list(request, project_id):
    """展示帖子列表，允许项目经理创建新帖子"""
    project = get_object_or_404(Project, id=project_id)

    if request.method == 'POST' and request.user == project.manager:  # 确保只有项目经理可以创建帖子
        title = request.POST.get('title')
        content = request.POST.get('content')
        image = request.FILES.get('image')

        if title and content:
            Post.objects.create(
                title=title,
                content=content,
                image=image,
                project=project,
                author=request.user
            )
            messages.success(request, '文章已创建')
            return redirect('post_list', project_id=project_id)
        else:
            messages.error(request, '请填写所有必填字段')

    posts = project.workspace_posts.all()  # 使用 `workspace_posts` 代替 `posts`
    context = {
        'project': project,
        'posts': posts,
    }
    return render(request, 'post_list.html', context)

@login_required
def delete_post(request, post_id):
    """删除帖子，允许作者和项目经理删除帖子"""
    post = get_object_or_404(Post, id=post_id)
    if request.user == post.author or request.user == post.project.manager:
        project_id = post.project.id
        post.delete()
        messages.success(request, '文章已删除')
        return redirect('post_list', project_id=project_id)
    else:
        messages.error(request, '您没有权限删除这篇文章')
        return redirect('post_list', project_id=post.project.id)

@login_required
def delete_project(request, project_id):
    """删除项目，允许项目经理删除项目"""
    project = get_object_or_404(Project, id=project_id)
    if request.user == project.manager:
        project.delete()
        messages.success(request, '项目已删除')
    else:
        messages.error(request, '您没有权限删除这个项目')
    return redirect('project_list')

@login_required
def update_post(request, post_id):
    """更新帖子，允许作者和管理员更新帖子"""
    post = get_object_or_404(Post, id=post_id)
    if post.author != request.user and not request.user.is_staff_member:
        messages.error(request, '你没有权限编辑这篇文章')
        return redirect('post_list', project_id=post.project.id)

    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        image = request.FILES.get('image')
        
        if title and content:
            post.title = title
            post.content = content
            if image:
                post.image = image
            post.save()
            messages.success(request, '文章更新成功')
            return redirect('post_list', project_id=post.project.id)
        else:
            messages.error(request, '请填写所有必填字段')

    context = {
        'post': post,
    }
    return render(request, 'post_list.html', context)

@login_required
def update_project(request, project_id):
    """更新项目，允许项目经理更新项目信息"""
    project = get_object_or_404(Project, id=project_id)

    if request.method == 'POST' and request.user == project.manager:
        title = request.POST.get('title')
        description = request.POST.get('description')
        start_date = request.POST.get('start_date')
        end_date = request.POST.get('end_date')
        staff_id = request.POST.get('staff')

        if title and description and start_date and end_date:
            project.title = title
            project.description = description
            project.start_date = start_date
            project.end_date = end_date

            if staff_id:
                try:
                    staff = User.objects.get(id=staff_id, is_staff_member=True)
                    project.manager = staff
                except User.DoesNotExist:
                    messages.error(request, '选择的项目管理者不存在')

            project.save()
            messages.success(request, '项目已更新')
            return redirect('project_list')
        else:
            messages.error(request, '请填写所有必填字段')

    context = {
        'project': project,
        'staff_list': User.objects.filter(is_staff_member=True)  # 提供所有工作人员供选择
    }
    return render(request, 'project_list.html', context)
