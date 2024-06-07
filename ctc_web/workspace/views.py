from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Project, Staff

@login_required
def project_list(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        start_date = request.POST.get('start_date')
        end_date = request.POST.get('end_date')
        staff_id = request.POST.get('staff')

        if not staff_id:
            messages.error(request, '没有提供项目管理者信息')
            return redirect('project_list')

        try:
            staff = Staff.objects.get(id=staff_id)
            Project.objects.create(
                title=title,
                description=description,
                start_date=start_date,
                end_date=end_date,
                staff=staff
            )
            messages.success(request, '项目已创建')
        except Staff.DoesNotExist:
            messages.error(request, '选择的项目管理者不存在')
        return redirect('project_list')

    projects = Project.objects.all()
    managers = Staff.objects.all()  # 获取所有的项目管理者
    return render(request, 'project_list.html', {'projects': projects, 'managers': managers})

@login_required
def post_list(request, project_id):
    project = get_object_or_404(Project, id=project_id)
    
    if request.method == 'POST' and request.user == project.staff.user:
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
            return redirect('post_list', project_id=project_id)
    
    posts = project.posts.all()
    return render(request, 'post_list.html', {'project': project, 'posts': posts})

@login_required
def delete_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if request.user == post.author or request.user == post.project.staff.user:
        project_id = post.project.id
        post.delete()
        messages.success(request, '文章已删除')
        return redirect('post_list', project_id=project_id)
    else:
        messages.error(request, '您没有权限删除这篇文章')
        return redirect('post_list', project_id=post.project.id)

@login_required
def delete_project(request, project_id):
    project = get_object_or_404(Project, id=project_id)
    if request.user == project.staff.user:
        project.delete()
        messages.success(request, '项目已删除')
    else:
        messages.error(request, '您没有权限删除这个项目')
    return redirect('project_list')

@login_required
def update_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    
    if request.method == 'POST' and (request.user == post.author or request.user == post.project.staff.user):
        title = request.POST.get('title')
        content = request.POST.get('content')
        image = request.FILES.get('image')
        
        if title and content:
            post.title = title
            post.content = content
            if image:
                post.image = image
            post.save()
            messages.success(request, '文章已更新')
            return redirect('post_list', project_id=post.project.id)
    
    return render(request, 'post_list.html', {'post': post})

@login_required
def update_project(request, project_id):
    project = get_object_or_404(Project, id=project_id)
    
    if request.method == 'POST' and request.user == project.staff.user:
        title = request.POST.get('title')
        description = request.POST.get('description')
        start_date = request.POST.get('start_date')
        end_date = request.POST.get('end_date')
        staff_id = request.POST.get('staff')
        
        try:
            staff = Staff.objects.get(id=staff_id)
            project.staff = staff
            project.title = title
            project.description = description
            project.start_date = start_date
            project.end_date = end_date
            project.save()
            messages.success(request, '项目已更新')
            return redirect('project_list')
        except Staff.DoesNotExist:
            messages.error(request, '选择的项目管理者不存在')

    return render(request, 'project_list.html', {'project': project})
