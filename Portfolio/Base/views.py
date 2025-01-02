from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib import messages
from Base import models
from Base.models import Contact
# Create your views here.
# def home(request):
#     return HttpResponse('Hello from the other side')

def home(request):
    return render(request,'home.html')

def contact(request):
    if request.method=="POST":
        print('post')
        name=request.POST.get('name')
        email=request.POST.get('email')
        content=request.POST.get('content')
        phnumber=request.POST.get('phnumber')
        print(name,email,content,phnumber)

        if len(name)>1 and len(name)<40:
            pass
        else:
            messages.error(request,'Length of name should be greater than 2 and less than 40')
            return render(request,'home.html')
        
        if len(email)>1 and len(email)<100:
            pass
        else:
            messages.error(request,'Length of email should be greater than 2 and less than 100')
            return render(request,'home.html')
        
        if len(content)>1 and len(content)<400:
            pass
        else:
            messages.error(request,'Length of Content should be greater than 2 and less than 400')
            return render(request,'home.html')
        
        if len(phnumber)>1 and len(phnumber)<20:
            pass
        else:
            messages.error(request,'Length of Number should be greater than 2 and less than 13')
            return render(request,'home.html')
        ins=models.Contact(name=name,email=email,content=content,phnumber=phnumber)
        ins.save()
        messages.success(request,'Thank You for Contacting Me || Your Message has been saved')
        print('data has been saved in the database')
        print('the request is no pass')
        return redirect('home')
    
    return render(request,'home.html')
