#from django.conf.urls import urls
from django.urls import path
from django.conf.urls import include
from . import views

app_name='questionsApp'

urlpatterns=[
    path('',views.question_list, name="question_list_url"),
    path('ask/',views.question_create, name="question_create_url"),
    #path('<slug:my_slug>/',views.question_detail, name="question_detail_url"),
    path('<slug:my_slug>/',views.question_detail, name="question_detail_url"),
    #<slug:my_slug> is a path converter that captures a string consisting of ASCII letters, numbers, hyphens, or underscores and assigns it to the variable my_slug. 
    #path('<int:questionObj_id>/',views.question_detail, name="question_detail_url"),
    #trying calling the objects here by ID instead of slug since using slugs doesnt currently work on this particular sub-app
    
]


