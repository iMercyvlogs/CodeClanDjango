from django import forms
from .import models   #the 'dot' represents 'current directory'


class CreatePost(forms.ModelForm):   #shows the kind of form we are using in this case;
    #form that allows for filling in of model attributes in UI
    class Meta:    #attributes
        model=models.PostClass    #tells which particular model we are working with
        fields=['title','body','slug','snippet']   #choose which particular fields/attributes we want to be displayed for filling
        #date field is ommitted since it is automatically generated and not filled by user
        