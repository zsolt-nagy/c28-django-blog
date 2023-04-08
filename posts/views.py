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


def new_post(request):
    if request.method == 'POST':
        try:
            post = Blogpost.objects.create(
                title=request.POST.get('title'),
                author=request.POST.get('author'),
                description=request.POST.get('description'),
            )
            post.save()
            context = {
                'title': 'The post has been created',
                'show_form': False,
            }
        except:
            context = {
                'title': 'The post could not be created. Try again.',
                'show_form': True,
            }
    else:
        context = {
            'title': 'New Post',
            'show_form': True,
        }
    return render(request, 'posts/new_post.html', context)
