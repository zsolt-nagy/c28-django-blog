from django.shortcuts import render
from .models import Blogpost

# Create your views here.


def index(request):
    context = {
        'title': 'blog home',
    }
    return render(request, 'posts/index.html', context)


def posts(request):
    posts = Blogpost.objects.all()
    context = {
        'count': posts.count(),
        'title': 'blogposts',
        'posts': posts
    }
    return render(request, 'posts/posts.html', context)


def post(request, post_id):
    try:
        post = Blogpost.objects.get(pk=post_id)
        context = {
            'exists': True,
            'post': post,
            'title': post.title,
        }
    except Blogpost.DoesNotExist:
        context = {
            'exists': False,
            'title': 'The post you are looking for does not exist',
        }
    return render(request, 'posts/post.html', context)
