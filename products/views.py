from django.shortcuts import render

from .forms import Productform,RawProductForm

from .models import Product

def product_create_view(request):
    my_form=RawProductForm(request.GET)
    if request.method=="POST":
        my_form=RawProductForm(request.POST)
        if my_form.is_valid():
            print(my_form.cleaned_data)
            my_form.save()
        else:
            print(my_form.errors)
    context={
        "form":my_form
    }
    return render(request,"product/product_create.html",context)



# def product_create_view(request):
#     form=Productform(request.POST or None)
#     if form.is_valid():
#         form.save()
#         form=Productform()

#     context={
#         'form':form
#     }
#     return render(request,"product/product_create.html",context)


# def product_create_view(request):
#     print(request.GET)
#     print(request.POST)
#     if request.method=="POST":
#         title=request.POST.get('title')
#         context={}
#     return render(request,"product/product_create_raw.html",context)


def product_detail_view(request):
    obj=Product.objects.get(id=1)
    # context={
    #     'title':obj.title,
    #     'description':obj.description
    # }
    context={
        'object':obj
    }
 
    return render(request,"product/detail.html",context)

    