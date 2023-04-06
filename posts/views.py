from django.shortcuts import render
from .models import Blogpost

# Create your views here.


def index(request):
    return render(request, 'posts/index.html')


def post(request):
    count = Blogpost.objects.all().count()
    context = {
        'count': count,
    }
    return render(request, 'posts/post.html', context)
