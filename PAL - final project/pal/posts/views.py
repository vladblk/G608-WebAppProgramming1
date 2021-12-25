from django.shortcuts import render
from django.http import HttpResponse
from .models import Post, Comment

# Create your views here.

def index(request):
    posts = Post.objects.all().order_by('-created')

    context = {
    'posts': posts
    }

    return render(request, 'posts/home.html', context)

def post(request, pk):
    post = Post.objects.get(id=pk)
    comments = Comment.objects.all().order_by('-created')

    context = {
    'post': post,
    'comments': comments
  }

    return render(request, 'posts/post.html', context)