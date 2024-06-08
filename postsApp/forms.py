from django import forms
from .import models   #the 'dot' represents 'current directory'
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column
from .models import PostClass


class CreatePost(forms.ModelForm):   #shows the kind of form we are using in this case;
    #form that allows for filling in of model attributes in UI
    class Meta:    #attributes
        model=models.PostClass    #tells which particular model we are working with
        fields=['title','body','slug','snippet','tags',]   #choose which particular fields/attributes we want to be displayed for filling
        #date field is ommitted since it is automatically generated and not filled by user
        

    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self.helper = FormHelper()
    #     self.helper.layout = Layout(
    #         Row(
    #             Column('title', css_class='form-group col-6'),
    #             Column('slug', css_class='form-group col-6'),
    #             css_class='form-row'
    #         ),
    #         'body',
    #         'snippet',
    #         'tags',
    #         Submit('submit', 'Submit', css_class='btn-primary')
    #     )



class CommentForm(forms.ModelForm):
    class Meta:
        model=models.PostCommentClass
        fields=['comment_id','comment','commenter','commented_post','parent_comment']

    def __init__(self, *args,**kwargs):
        super().__init__(*args,**kwargs)
        self.fields['comment'].widget.attrs.update({'class':'form-control'})
        self.fields['commenter'].widget.attrs.update({'class':'form-control'})