from django.http import HttpResponse

#import the possibility to render html pages
from django.shortcuts import render


#create functions that will be linked to the paths in url.py
#these determines what happens each time the request is sent/page is clicked on

def homepage(request):
    #return HttpResponse('homepage')
    return render(request,'Home.html')

def questions(request):
    #return HttpResponse('questions')
    return render(request,'questions.html')

# def posts(request):
#     #return HttpResponse('posts')
#     return render(request,'posts.html')


