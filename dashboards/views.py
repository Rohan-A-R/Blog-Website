from django.shortcuts import get_object_or_404, redirect, render
from blogs.models import Blog, Category
from django.contrib.auth.decorators import login_required
from .forms import BlogPostForm, CategoryForm, adduserform,EditUserform
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User

# Create your views here.

@login_required(login_url='login')
def dashboard(request):
    category_count=Category.objects.all().count()
    blogs_count=Blog.objects.all().count()
    context={
        'category_count':category_count,
        'blogs_count':blogs_count,
    }
    return render(request,'dashboard/dashboard.html',context)

@login_required(login_url='login')
def categories(request):
    return render(request,'dashboard/categories.html')

@login_required(login_url='login')
def add_category(request):
    if request.method=='POST':
        form=CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('categories')
    form=CategoryForm
    context={
        'form':form,
    }
    return render(request,'dashboard/addcategory.html',context)

@login_required(login_url='login')
def edit_category(request,pk):
    category=get_object_or_404(Category,pk=pk)
    if request.method=='POST':
        form=CategoryForm(request.POST,instance=category)
        if form.is_valid():
            form.save()
            return redirect('categories')
    form=CategoryForm(instance=category)
    context={
        'form':form,
        'category':category
    }
    return render(request,'dashboard/edit_category.html',context)


def delete_category(request,pk):
    category=get_object_or_404(Category,pk=pk)
    category.delete()
    return redirect('categories')

def posts(request):
    posts=Blog.objects.all()
    context={
        'posts':posts,
    }
    return render(request,'dashboard/posts.html',context)

def add_post(request):
    if request.method =='POST':
        form=BlogPostForm(request.POST,request.FILES)  #important
        if form.is_valid():
            post=form.save(commit=False)  #temp saving
            post.author=request.user
            post.save()
            title=form.cleaned_data['title']
            post.slug=slugify(title) 
            post.save()
            return redirect('posts')
        else:
            print('form is not valid')
            print(form.errors)
    form=BlogPostForm()
    context={
        'form':form
    }
    return render(request,'dashboard/add_post.html',context)


def edit_post(request,pk):
    post=get_object_or_404(Blog,pk=pk)
    if request.method == 'POST':
        form =BlogPostForm(request.POST,request.FILES,instance=post)
        if form.is_valid():
            post=form.save()
            title=form.cleaned_data['title']
            post.slug=slugify(title) + '-'+str(post.id)
            post.save()
            return redirect('posts')
    form=BlogPostForm(instance=post)
    context={
        'form':form,
        'post':post
    }
    return render(request,'dashboard/edit_post.html',context)



def delete_post(request,pk):
    post=get_object_or_404(Blog,pk=pk)
    post.delete()
    return redirect('posts')

def users(request):
    users=User.objects.all()
    context={
        'users':users
    }
    return render(request,'dashboard/users.html.',context)

def add_user(request):
    if request.method=='POST':
        form =adduserform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('users')
        else:
            print(form.errors)
    form=adduserform()
    context={
        'form':form
    }
    return render(request,'dashboard/add_user.html',context)


def edit_user(request,pk):
    user=get_object_or_404(User,pk=pk)
    if request.method=='POST':
        form=EditUserform(request.POST,instance=user)
        if form.is_valid():
            form.save()
            return redirect('users')
    form=EditUserform(instance=user)
    context={
        'form':form,
    }
    return render(request,'dashboard/edit_user.html',context)


def delete_user(request,pk):
    user=get_object_or_404(User,pk=pk)
    user.delete()
    return redirect('users')

