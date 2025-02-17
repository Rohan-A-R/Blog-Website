
from django.shortcuts import redirect, render

from blog_main.forms import Registrationform
from blogs.models import About, Blog, Links
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import auth


def home(request):
    featured_post=Blog.objects.filter(is_fetured=True,status='Published').order_by('-updated_at')
    recent_post=Blog.objects.filter(is_fetured=False,status='Published').order_by('-updated_at')
    try:
        about=About.objects.get()
    except:
        about=None

    context={
        'featured_post':featured_post,
        'recent_post':recent_post,
        'about':about,
    }
    return render(request,'home.html',context)


def register(request):
    if request.method == 'POST':
        form=Registrationform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('register')
    else:
        form=Registrationform()
    context={
        'form':form,
    }
    return render(request,'register.html',context)

def login(request):
    if request.method=='POST':
        form=AuthenticationForm(request,request.POST)
        if form.is_valid():
            username= form.cleaned_data['username']
            password= form.cleaned_data['password']

            user=auth.authenticate(username=username,password=password)
            if user is not None:
                auth.login(request,user)
            return  redirect('dashboard') 
    form=AuthenticationForm()
    context={
        'form':form
    }
    return render(request,'login.html',context)

def logout(request):
    auth.logout(request)
    return redirect('home')