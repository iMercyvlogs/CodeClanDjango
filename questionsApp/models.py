from django.db import models

# Create your models here.
from django.db import models

# Create your models here.
#models are classes in django that detail each table in DB
class QuestionClass(models.Model):
    title= models.CharField(max_length=100)
    #slug=models.SlugField()
    body= models.TextField()
    
    #add snippet section, we'll add a feature/python framework for checking and highlighting syntax eventually
    snippet=models.TextField(blank=True, null=True)
    #add tags
    
    #add author
    date=models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.title
    
    def shortened_qtn(self):
        return self.body[:50]+ "..."
    