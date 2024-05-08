from django.shortcuts import render
from .models import Product,Tag


def index(request):
    return render(request,'index.html')


def shop(request):
    product=Product.objects.all()
    context={
        'product':product
    }
    return render(request,'shop.html',context)


def about(request):
    return render(request,'about.html')



def services(request):
    return render(request,'services.html')


def contact(request):
    return render(request,'contact.html')


def blog(request):
    product=Product.objects.all()
    context={
        'product':product
    }
    return render(request,'blog.html',context)


def cart(request):
    return render(request,'cart.html')


def checkout(request):
    return render(request,'checkout.html')


def thankyou(request):
    return render(request,'thankyou.html')



def content(request):
    
    context={
        'data':'salam'
            }
    return render(request,'content.html',context)


def test(request):
    data=''
    if request.method=="POST":
        data = request.POST['soz']

    context={
        'data':data
    }

    return render(request,"test.html",context)