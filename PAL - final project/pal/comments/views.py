from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.contrib import messages
from posts import forms
from .models import Comment
from .forms import CommentForm
from posts.models import Post
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required(login_url='user:sign-in')
def update_comment(request, pk):
    # post = Post.objects.get(id=post_id)
    comment = Comment.objects.get(id=pk)
    form = CommentForm(instance=comment)

    if request.method == 'POST':
        form = CommentForm(request.POST, instance=comment)
        next = request.POST.get('next', '/')

        if form.is_valid():
            form.save()

            messages.success(request, 'Successfully updated your comment!')

            return HttpResponseRedirect(next)
        else:
            messages.error(request, 'Something went wrong...')

    context = {
        'comment': comment,
        'form': form
    }

    return render(request, 'comments/comment_form.html', context)


@login_required(login_url='user:sign-in')
def delete_comment(request, pk):
    comment = Comment.objects.get(id=pk)

    if request.user != comment.user:
        return render(request, 'not_allowed.html')

    if request.method == 'POST':
        next = request.POST.get('next', '/')
        comment.delete()

        messages.success(request, 'Successfully deleted your comment!')

        return HttpResponseRedirect(next)

    context = {
        'to_delete': comment
    }

    return render(request, 'delete.html', context)