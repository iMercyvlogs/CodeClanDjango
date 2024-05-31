"""
URL configuration for CodeClanDjango project.

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
from django.conf.urls import include
#import views file in same directory inorder to access funtions created there
#we'll use the functions to create paths for the urls created 
from .import views
#import files to allow the use of static files, bootstrap in this case
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


"""creating all required pages and corresponding urls/paths"""
urlpatterns = [
    
    path('admin/', admin.site.urls), # admin page
    path('',views.homepage, name="homepage_url"),# home page which redirects to main path
    

    #also link all urls from all other pages from other apps

    path('posts/',include('postsApp.urls')),#link to posts page
    path('questions/', include('questionsApp.urls')),#link to questions page
    path('accounts/', include('accountsApp.urls')),

]

#add static files to all existing paths in project
urlpatterns += staticfiles_urlpatterns()