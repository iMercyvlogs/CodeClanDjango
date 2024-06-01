from django.shortcuts import render, get_object_or_404,redirect
from .models import PostClass
from django.http import HttpResponse
from  django.contrib.auth.decorators import login_required
from .import forms


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
    if request.method=='POST':
        create_form=forms.CreatePost(request.POST)  #this post only brings data, not files
        #so in a case where we also wanted to upload files, we would need to add : request.FILES
        if create_form.is_valid():   #check that the data has been accurately collected, then ..
           instance=create_form.save(commit=False)  #commit=False asks compiler to hold-on for something to happen first before finally saving to db
            #save post in db
           instance.author=request.user  #associate created post to the particular user,author
           instance.save()  #now save to db
           return redirect('postsApp:post_list_url')

    else:
        create_form=forms.CreatePost()
    return render(request,'postsApp/post_create.html', {'form':create_form})