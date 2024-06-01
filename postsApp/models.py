from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class PostClass(models.Model):
    title=models.CharField(max_length=100)
    slug=models.SlugField()
    body=models.TextField()
    snippet=models.TextField(blank=True, null=True)
    date=models.DateTimeField(auto_now_add=True)
    author=models.ForeignKey(User,default=None,on_delete=models.CASCADE) #This specifies that if the referenced User object is deleted, the associated PostClass object should also be deleted.

    def __str__(self):
        return self.title
    

    #create a function that makes the posts to be diplayed in shortened form until when clicked then redirected to another page that displays desired post in full.
    def shortened_post(self):
        return self.body[:50]+"..."  #desired number of words to be displayed for starters is 50, the "..." appended to indicate there's more

