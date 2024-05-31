from django.urls import path
from django.conf.urls import include
from . import views

app_name='postsApp'

urlpatterns=[
    path('',views.post_list,name="post_list_url"),
    path('create/',views.post_create, name="post_create_url"),
    #make sure this path comes before the one that identifies each post by "slug"
    #because otherwise, compiler will start working on particular/preexisting post rather than creating a new one
    path('<slug:my_slug>/',views.post_detail, name="post_detail_url"),
    #<slug:my_slug> is a path converter that captures a string consisting of 
    #ASCII letters, numbers, hyphens, or underscores and assigns it to the variable my_slug. 
    
]
