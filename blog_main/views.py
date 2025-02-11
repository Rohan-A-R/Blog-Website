
from django.shortcuts import render

from blogs.models import Blog, Category


def home(request):
    featured_post=Blog.objects.filter(is_fetured=True,status='Published').order_by('-updated_at')
    recent_post=Blog.objects.filter(is_fetured=False,status='Published').order_by('-updated_at')
    print(recent_post)
    context={
        'featured_post':featured_post,
        'recent_post':recent_post,
    }
    return render(request,'home.html',context)