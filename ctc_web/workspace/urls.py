from django.urls import path
from .views import project_list, update_project, delete_project, post_list, update_post, delete_post

urlpatterns = [
    path('project/', project_list, name='project_list'),  # 项目列表页
    path('project/<int:project_id>/update/', update_project, name='update_project'),  # 更新项目
    path('project/<int:project_id>/delete/', delete_project, name='delete_project'),  # 删除项目
    path('project/<int:project_id>/posts/', post_list, name='post_list'),  # 帖子列表页
    path('posts/<int:post_id>/update/', update_post, name='update_post'),  # 更新帖子
    path('posts/<int:post_id>/delete/', delete_post, name='delete_post'),  # 删除帖子
]
