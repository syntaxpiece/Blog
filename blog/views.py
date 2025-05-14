from django.shortcuts import render
from .models import *

# Create your views here.

def index (request):
    context = {
        'blogs' : Blog.objects.order_by('-id')[:6],
        'projects' : Project.objects.order_by('-id')[:6],
        'quote' : Quote.objects.last(),
    }
    return render(request, 'blog/index.html', context)


def projects (request):
    context = {
        'projects' : Project.objects.all(),
        'quote' : Quote.objects.last(),
    }
    return render(request, 'blog/projects.html', context)

def blog (request):
    context = {
        'blogs' : Blog.objects.all(),
        'quote' : Quote.objects.last(),
    }
    return render(request, 'blog/blog.html', context)