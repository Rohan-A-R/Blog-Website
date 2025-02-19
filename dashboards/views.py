from django.shortcuts import get_object_or_404, redirect, render
from blogs.models import Blog, Category
from django.contrib.auth.decorators import login_required
from .forms import CategoryForm

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

