from django.shortcuts import render,get_object_or_404
from .models import QuestionClass
from django.http import HttpResponse
# Create your views here.

def question_list(request):
    #create variable that stores all the objects in this class/model
    #order items based on time/date
    all_questions=QuestionClass.objects.all().order_by('date')
    return render(request,'questionsApp/question_list.html',{'all_questions':all_questions})


# def question_detail(request,my_slug):
#     return HttpResponse(my_slug)

# def question_detail(request,questionObj_id):
#     theQuestion=QuestionClass.objects.get(id=questionObj_id)
#     #theQuestion=get_object_or_404(QuestionClass,pk=questionObj_id)
#     return render(request, 'questionsApp/question_detail.html', {'theQuestion':theQuestion})

def question_detail(request,my_slug):

    #return HttpResponse(my_slug)
    theQuestion=QuestionClass.objects.get(slug=my_slug)
    #print(thePost) commented, as it obviously does not work.
    #slug here represents the attribute "slug" in the class PostClass
    return render(request, 'questionsApp/question_detail.html', {'theQuestion':theQuestion})