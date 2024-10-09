"""
URL configuration for womenproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from womenapp.views import index,User_Reg,adv_reg,loginview
from womenapp import admin_urls,user_urls,adv_urls

urlpatterns = [
    path('',index.as_view()),
    path('user_reg',User_Reg.as_view(),name='user_reg'),
    path('adv_reg',adv_reg.as_view(),name='adv_reg'),
    path('admin/',admin_urls.urls()),
    path('user/',user_urls.urls()),
    path('adv/',adv_urls.urls()),
    path('login/',loginview.as_view(),name='login')




]
if settings.DEBUG:
    urlpatterns+=static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

