from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import login,logout


# Create your views here.
def signup_view(request):
    if request.method=='POST': #check if current task is to put/post info into the DB,(as in, it meets up to all pw requirements) then do the following
       signup_form=UserCreationForm(request.POST)#then apply django's inbuilt features for forms
       if signup_form.is_valid(): #then update DB with data from the form
           user=signup_form.save()
           #log user in
           login(request,user)
           return redirect('postsApp:post_list_url') #for now, lets redirect to the questions page, 
           #eventually update the code to only make users signup when they want to upload a code
    
    else: #otherwise, if it is a get request, then display the blank form(re-enter info)with warning
        signup_form= UserCreationForm()
    return render(request,'accountsApp/signup.html', {'form':signup_form})

def login_view(request):
    if request.method=='POST': #chwck that task is to post on the condition that it meets up to all pw requirements) then do the following
        login_form=AuthenticationForm(data=request.POST)  #check data filled, for validity
        if login_form.is_valid():         #if it's valid, then log user in/redirect in this case
        #log user in
            user=login_form.get_user() #create variable and query the info of the current user
            login(request,user)        #perform the inbuilt action of logging user in

            if 'next' in request.POST:
                return redirect(request.POST.get('next'))
            else:
                return redirect('postsApp:post_list_url') #for now, lets redirect to the questions page, 
    else:
        login_form=AuthenticationForm()   #otherwise, if data incorrect, then display same form

    return render(request, 'accountsApp/login.html', {'form':login_form})


def logout_view(request):
    if request.method=='POST':
        logout(request)
        return redirect('postsApp:post_list_url')