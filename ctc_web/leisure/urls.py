from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post_action/', views.post_action, name='post_action'),
]
