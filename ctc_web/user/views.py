from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import User
from workspace.models import Project
from django.contrib.auth import authenticate, login, logout

def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')  # 登录成功后跳转到首页
        else:
            messages.error(request, '用户名或密码无效')
    return render(request, 'user/login.html')

def user_logout(request):
    logout(request)
    return redirect('login')  # 登出后跳转到登录页

def user_register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        user_type = request.POST.get('user_type')  # 获取用户身份

        if password != confirm_password:
            messages.error(request, '两次密码不一致')
            return redirect('register')
        
        if user_type not in ['staff', 'member']:  # 验证用户身份
            messages.error(request, '请选择有效的身份类型')
            return redirect('register')

        try:
            user = User.objects.create_user(username=username, password=password)
            user.user_type = user_type  # 设置用户身份
            if user_type == 'staff':
                user.is_staff_member = True  # 设置为干部
            user.save()
            login(request, user)
            return redirect('index')  # 注册成功后跳转到首页
        except Exception as e:
            messages.error(request, '创建用户时出错: ' + str(e))
            return redirect('register')
    
    return render(request, 'user/register.html')

@login_required
def manage_project_permissions(request, project_id):
    project = get_object_or_404(Project, id=project_id)

    if request.user != project.manager:
        messages.error(request, '您没有权限管理此项目')
        return redirect('project_list')
    
    if request.method == 'POST':
        user_id = request.POST.get('user_id')
        action = request.POST.get('action')
        
        user = get_object_or_404(User, id=user_id)
        
        if action == 'make_manager':
            user.is_staff_member = True
            user.save()
            messages.success(request, f'{user.username} 现在是项目管理员')
        elif action == 'remove_manager':
            user.is_staff_member = False
            user.save()
            messages.success(request, f'{user.username} 已被移除管理员角色')
    
    users = User.objects.all()
    return render(request, 'manage_project_permissions.html', {'project': project, 'users': users})
