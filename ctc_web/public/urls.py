from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # 根路径渲染 index.html
]
