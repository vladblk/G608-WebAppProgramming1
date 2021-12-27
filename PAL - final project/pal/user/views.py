from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm

# Create your views here.

def signup(request):
    form = UserCreationForm()

    if request.method == 'POST':
        form = UserCreationForm(request.POST)

        if form.is_valid():
            new_user = form.save(commit=False) # save the form but don't commit to DB

            new_user.username = new_user.username.lower()
            new_user.save()

            return redirect('posts:index')


    context = {
        'form': form
    }

    return render(request, 'user/signup.html', context)