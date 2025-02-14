
from django.shortcuts import render

from blogs.models import About, Blog, Links


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