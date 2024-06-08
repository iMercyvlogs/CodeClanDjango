
from .models import QuestionClass
from django.http import HttpResponse

from django.shortcuts import render, get_object_or_404,redirect


from  django.contrib.auth.decorators import login_required
from .import forms
from taggit.models import Tag

from django.contrib import messages #a kind of error handler
 

# Create your views here.

def question_list(request):
    #create variable that stores all the objects in this class/model
    #order items based on time/date
    all_questions=QuestionClass.objects.all().order_by('date')
    return render(request,'questionsApp/question_list.html',{'all_questions':all_questions})



def question_detail(request,my_slug):

    #return HttpResponse(my_slug)
    #theQuestion=QuestionClass.objects.get(slug=my_slug)
    theQuestion = get_object_or_404(QuestionClass, slug=my_slug)
    #slug here represents the attribute "slug" in the class QuestionClass
    return render(request, 'questionsApp/question_detail.html', {'theQuestion':theQuestion})


@login_required(login_url="/accounts/login/")
def question_create(request):
    common_tags=QuestionClass.tags.most_common()[:6]
    if request.method=='POST':
        question_form=forms.AskQuestionClass(request.POST)  #this post only brings data, not files
        #so in a case where we also wanted to upload files, we would need to add : request.FILES
        if question_form.is_valid():   #check that the data has been accurately collected, then ..
           newquestion=question_form.save(commit=False)  #commit=False asks django to hold-on for something to happen first before finally saving to db
            
           newquestion.author=request.user  #associate created post to the particular user,author
           newquestion.save()  #now save to db
           #without next line, tags won't be saved
           question_form.save_m2m()


           return redirect('questionsApp:question_list_url')

    else:
        question_form=forms.AskQuestionClass()
    return render(request,'questionsApp/question_create.html', {'form':question_form})



def tagged(request, my_slug):
    tag=get_object_or_404(Tag, slug=my_slug)
    #Filter posts by tag name
    filteredQuestions=QuestionClass.objects.filter(tags=tag)
    
    # context= {
    #     'tag':tag
    #     'posts':posts
    # }

    return render(request, 'questionsApp/question_create.html',{'allQuestions':filteredQuestions})