from django.shortcuts import render, redirect
from .models import Comment
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required(login_url='user:sign-in')
def delete_comment(request, pk):
    comment = Comment.objects.get(id=pk)

    if request.user != comment.user:
        return render(request, 'not_allowed.html')

    if request.method == 'POST':
        comment.delete()

        return redirect('posts:index')
        # return redirect(request.META.get('HTTP_REFERER')) # NOT WORKING!!!

    context = {
        'to_delete': comment
    }

    return render(request, 'delete.html', context)