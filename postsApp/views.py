from django.shortcuts import render, get_object_or_404
from .models import PostClass
from django.http import HttpResponse
from  django.contrib.auth.decorators import login_required

# Create your views here.

def post_list(request):
    #creating variables that stores all the objects in this class/model
    #order the items based on date of entry
    all_posts=PostClass.objects.all().order_by('date')
    return render(request, 'postsApp/post_list.html',{'all_posts':all_posts})


def post_detail(request,my_slug):

    #return HttpResponse(my_slug)
    thePost=PostClass.objects.get(slug=my_slug)
    #print(thePost) commented, as it obviously does not work.
    #slug here represents the attribute "slug" in the class PostClass
    return render(request, 'postsApp/post_detail.html', {'thePost':thePost})
    

#to allow the possibility for creating new posts only by users who have loggedin/signedup, we use the decorator ..
#also redirect users to login page if they aren't loggedin
@login_required(login_url="/accounts/login/")
def post_create(request):
    return render(request,'postsApp/post_create.html')