"""
URL configuration for ctc_web project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from workspace.urls import urlpatterns as workspaceURL
from leisure.urls import urlpatterns as leisureURL
from public.urls import urlpatterns as publicURL
urlpatterns = [
     path('', include(publicURL)), 
    path('admin/', admin.site.urls),
    path('workspace/', include(workspaceURL)),
    path('leisure/', include(leisureURL)),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

