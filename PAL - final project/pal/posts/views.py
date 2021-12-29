from django.http.response import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from posts.forms import PostForm
from posts.models import Post
from comments.models import Comment

# Create your views here.

def index(request):
    posts = Post.objects.all().order_by('-created')

    context = {
        'posts': posts
    }

    return render(request, 'posts/home.html', context)


def post(request, pk):
    post = Post.objects.get(id=pk)
    comments = post.comment_set.all().order_by('-created') # get the comments from each post

    if request.method == 'POST':
        Comment.objects.create(
            user = request.user,
            post = post,
            body = request.POST.get('comment')
        )

        return redirect('posts:post', pk=post.id)

    context = {
    'post': post,
    'comments': comments
  }

    return render(request, 'posts/post.html', context)


@login_required(login_url='user:sign-in')
def create_post(request):
    form = PostForm()

    if request.method == 'POST':
        form = PostForm(request.POST)

        if form.is_valid():
            form.save()

            return redirect('posts:index')


    context = {
        'form': form
    }

    return render(request, 'posts/post_form.html', context)


@login_required(login_url='user:sign-in')
def update_post(request, pk):
    post = Post.objects.get(id=pk)
    form = PostForm(instance=post) # get the instance of the specific post - prefill the inputs in the form

    if request.user != post.user:
        return render(request, 'not_allowed.html')

    if request.method == 'POST':
        form = PostForm(request.POST, instance=post) # if instance is not specified here again, it will create a new post instead of updating
        next = request.POST.get('next', '/')

        if form.is_valid():
            form.save()

            return HttpResponseRedirect(next)

    context = {
        'post': post,
        'form': form,
    }

    return render(request, 'posts/post_form.html', context)


@login_required(login_url='user:sign-in')
def delete_post(request, pk):
    post = Post.objects.get(id=pk)

    if request.user != post.user:
        return render(request, 'not_allowed.html')

    if request.method == 'POST':
        post.delete()

        return redirect('posts:index')
        # return redirect(request.META.get('HTTP_REFERER')) # NOT WORKING!!!

    context = {
        'to_delete': post
    }

    return render(request, 'delete.html', context)