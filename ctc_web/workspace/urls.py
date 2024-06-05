from django.urls import path
from . import views

urlpatterns = [
    path('project/', views.project_list, name='project_list'),
    path('project/<int:project_id>/', views.post_list, name='post_list'),
    path('post/delete/<int:post_id>/', views.delete_post, name='delete_post'),
    path('project/delete/<int:project_id>/', views.delete_project, name='delete_project'),
    path('post/update/<int:post_id>/', views.update_post, name='update_post'),
    path('project/update/<int:project_id>/', views.update_project, name='update_project'),
]
