from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def homepage_view(request,*args,**kwargs):
    print(args,kwargs)
    print(request.user)
    return render(request,"home.html",{})  #String of html code 


def contact_view(request,*args,**kwargs):
    my_context={
        "my_text":"this is about us",
        "my_number":123,
        "my_list":[1,2,3,4]
    }
    return render(request,"contact.html",my_context)  #Contact View

