from django.db import models
from django.contrib.auth.models import User

from taggit.managers import TaggableManager


# Create your models here.


class PostClass(models.Model):
    title=models.CharField(max_length=100,unique=True)
    slug=models.SlugField(max_length=100,unique=True)
    body=models.TextField()
    snippet=models.TextField(blank=True, null=True)
    date=models.DateTimeField(auto_now_add=True)
    author=models.ForeignKey(User,default=None,on_delete=models.CASCADE) #This specifies that if the referenced User object is deleted, the associated PostClass object should also be deleted.

    tags=TaggableManager()



    def __str__(self):
        return self.title
    

    #create a function that makes the posts to be diplayed in shortened form until when clicked then redirected to another page that displays desired post in full.
    def shortened_post(self):
        return self.body[:50]+"..."  #desired number of words to be displayed for starters is 50, the "..." appended to indicate there's more


class PostCommentClass(models.Model):
    comment_id=models.AutoField(primary_key=True)
    comment=models.TextField()
    commenter=models.ForeignKey(User, on_delete=models.CASCADE)
    commented_post=models.ForeignKey(PostClass,on_delete=models.CASCADE)
    parent_comment=models.ForeignKey('self',on_delete=models.CASCADE,null=True)
    #allows comments to have a hierarchical parent-child relationship//nested structure//self-referential foreign key=> one comment can be the child of another
    created_at=models.DateTimeField(auto_now_add=True)
