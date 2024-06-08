from django import forms
from .import models   #the 'dot' represents 'current directory'
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column
from .models import QuestionClass


class AskQuestionClass(forms.ModelForm):   #shows the kind of form we are using in this case;
    #form that allows for filling in of model attributes in UI
    class Meta:    #attributes
        model=models.QuestionClass    #tells which particular model we are working with
        fields=['title','body','slug','snippet','tags',]   #choose which particular fields/attributes we want to be displayed for filling
        #date field is ommitted since it is automatically generated and not filled by user