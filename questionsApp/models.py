from django.db import models
from django.contrib.auth.models import User
from taggit.managers import TaggableManager

# Create your models here.


# Create your models here.
#models are classes in django that detail each table in DB

    

class QuestionClass(models.Model):
    title= models.CharField(max_length=100)
    slug=models.SlugField()
    body= models.TextField()
    #add snippet section, we'll add a feature/python framework for checking and highlighting syntax eventually
    snippet=models.TextField(blank=True, null=True)
    
    date=models.DateTimeField(auto_now_add=True)
    author=models.ForeignKey(User,default=None,on_delete=models.CASCADE) #This specifies that if the referenced User object is deleted, the associated QuestionClass object should also be deleted.
    #add tags
    tags=TaggableManager()

    def __str__(self):
        return self.title
    
    def shortened_qtn(self):
        return self.body[:50]+ "..."
    

class AnswerClass(models.Model):
    comment_id=models.AutoField(primary_key=True)
    comment=models.TextField()
    commenter=models.ForeignKey(User, on_delete=models.CASCADE)
    commented_post=models.ForeignKey(QuestionClass,on_delete=models.CASCADE)
    parent_comment=models.ForeignKey('self',on_delete=models.CASCADE,null=True)
    snippet=models.TextField(blank=True, null=True)
    #allows comments to have a hierarchical parent-child relationship//nested structure//self-referential foreign key=> one comment can be the child of another
    created_at=models.DateTimeField(auto_now_add=True)
    