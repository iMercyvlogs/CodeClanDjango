from django.shortcuts import render, get_object_or_404,redirect
from .models import PostClass,PostCommentClass #import all created classes/models in this subapp

from  django.contrib.auth.decorators import login_required
from .import forms
from taggit.models import Tag

from django.contrib import messages #a kind of error handler
from .forms import CommentForm 


# Create your views here.

def post_list(request):
    #creating variables that stores all the objects in this class/model
    #order the items based on date of entry
    all_posts=PostClass.objects.all().order_by('date')
    return render(request, 'postsApp/post_list.html',{'all_posts':all_posts})

def post_detail(request, my_slug):
    thepost = get_object_or_404(PostClass, slug=my_slug)
    comments = PostCommentClass.objects.filter(commented_post=thepost)

    if request.method == 'POST':
        comment_form = CommentForm(request.POST) #use djangos inbuilt comment feature to collect data from user and save in "comment_form"
        if comment_form.is_valid():   #check if it is valid then..
        
            new_comment = comment_form.save(commit=False)   #save data from the form into new_comment" but don't update DB just yet
            new_comment.commented_post = thepost    #associate the comment to the post that was commented on, then ..
            new_comment.save()   #update DB
            return redirect('post_detail', my_slug=thepost.slug)   #redirect user back to detail page with target slug
        

    else:
        comment_form = CommentForm()  #if not a POST request, then stay on same commentform page

    context = {
        'commented_post': thepost,
        'comments': comments,
        'comment_form': comment_form
    }

    return render(request, 'postsApp/post_detail.html', context)

# def post_detail(request,my_slug):

#     thePost=PostClass.objects.get(slug=my_slug)
    
#     #slug here represents the attribute "slug" in the class PostClass
#     return render(request, 'postsApp/post_detail.html', {'thePost':thePost})
    

#to allow the possibility for creating new posts only by users who have loggedin/signedup, we use the decorator ..
#also redirect users to login page if they aren't loggedin
@login_required(login_url="/accounts/login/")
def post_create(request):
    common_tags=PostClass.tags.most_common()[:3]
    if request.method=='POST':
        create_form=forms.CreatePost(request.POST)  #this post only brings data, not files
        #so in a case where we also wanted to upload files, we would need to add : request.FILES
        if create_form.is_valid():   #check that the data has been accurately collected, then ..
           newpost=create_form.save(commit=False)  #commit=False asks django to hold-on for something to happen first before finally saving to db
           newpost.author=request.user  #associate created post to the particular user,author
           newpost.save()  #now save to db
           #without next line, tags won't be saved
           create_form.save_m2m()


           return redirect('postsApp:post_list_url')

    else:
        create_form=forms.CreatePost()
    return render(request,'postsApp/post_create.html', {'form':create_form})



def tagged(request, my_slug):
    tag=get_object_or_404(Tag, slug=my_slug)
    #Filter posts by tag name
    filteredPosts=PostClass.objects.filter(tags=tag)
    
    # context= {
    #     'tag':tag
    #     'posts':posts
    # }

    return render(request, 'postsApp/post_create.html',{'allPosts':filteredPosts})



# def add_comment(request):
#     if request.method=='POST':
#         comment=request.POST.get('comment')
#         commenter=request.commenter
#         post_id=request.POST.get('post_id')
#         post=PostClass.objects.get(id=post_id)

#         commentObj=PostCommentClass(comment=comment,user=commenter,post=post)
#         commentObj.save()
#         messages.success(request,"Comment added Successfully!!")

#     else:
#         messages.error(request,"an error occurred while adding comment")

#     return redirect('post_detail_url',post.slug)#pass "post.slug" as an arguement to the function with url name"post_detail_url"
#          #"post.slug" is queried from the object with id:post_id in if-statement above