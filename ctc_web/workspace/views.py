from django.shortcuts import render, get_object_or_404, redirect
from .models import Post, Project, Staff
from .forms import ProjectForm

# List and Create Posts for a Project
def post_list(request, project_id):
    project = get_object_or_404(Project, id=project_id)
    
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        image = request.FILES.get('image')
        
        if title and content:
            Post.objects.create(
                title=title,
                content=content,
                image=image,
                project=project
            )
            return redirect('post_list', project_id=project_id)
    
    posts = project.posts.all()
    return render(request, 'post_list.html', {'project': project, 'posts': posts})

# List and Create Projects
def project_list(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        start_date = request.POST.get('start_date')
        end_date = request.POST.get('end_date')
        staff_id = request.POST.get('staff')
        
        if staff_id:
            staff = Staff.objects.get(id=staff_id)
            
            Project.objects.create(
                title=title,
                description=description,
                start_date=start_date,
                end_date=end_date,
                staff=staff
            )
    
    project_form = ProjectForm()
    projects = Project.objects.all()
    return render(request, 'project_list.html', {'project_form': project_form, 'projects': projects})

# Delete a Post
def delete_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    project_id = post.project.id
    post.delete()
    return redirect('post_list', project_id=project_id)

# Delete a Project
def delete_project(request, project_id):
    project = get_object_or_404(Project, id=project_id)
    project.delete()
    return redirect('project_list')

# Update a Post
def update_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    
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
            return redirect('post_list', project_id=post.project.id)
    
    return render(request, 'post_list.html', {'post': post})

# Update a Project
def update_project(request, project_id):
    project = get_object_or_404(Project, id=project_id)
    
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        start_date = request.POST.get('start_date')
        end_date = request.POST.get('end_date')
        staff_id = request.POST.get('staff')
        
        if staff_id:
            staff = Staff.objects.get(id=staff_id)
            project.staff = staff
        
        project.title = title
        project.description = description
        project.start_date = start_date
        project.end_date = end_date
        project.save()
        return redirect('project_list')
    
    return render(request, 'project_list.html', {'project': project})
