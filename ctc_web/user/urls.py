from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('register/', views.user_register, name='register'),
    path('projects/<int:project_id>/manage_permissions/', views.manage_project_permissions, name='manage_project_permissions'),  # 项目权限管理
]
