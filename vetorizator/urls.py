"""
URL configuration for vetorizator project.

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
from django.urls import path
from app import views
from django.conf import settings
from django.conf.urls.static import static
from app.views import upload_image

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', views.index),
    path('', views.upload_image, name='upload_image'),
    # path('upload-button/', views.upload_button, name='upload_button')
    path('convert/', views.convert, name='convert_view'),
    path('download_image/', views.download_image, name='download_image'),
    path('download_last_image/', views.download_last_image, name='download_last_image'),  # Add this line
] 
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)