from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required

def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')  # 确保你有名为 'index' 的 URL 模式
        else:
            messages.error(request, 'Invalid username or password')
    return render(request, 'user/login.html')

def user_logout(request):
    logout(request)
    return redirect('login')

def user_register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        
        if password != confirm_password:
            messages.error(request, 'Passwords do not match')
            return redirect('register')
        
        try:
            user = User.objects.create_user(username=username, password=password)
            user.save()
            login(request, user)
            return redirect('index')  # 确保你有名为 'index' 的 URL 模式
        except Exception as e:
            messages.error(request, 'Error creating user: ' + str(e))
            return redirect('register')
    
    return render(request, 'user/register.html')
