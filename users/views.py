from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import UserRegisterForm
from django.contrib.auth.decorators import login_required
from blog.models import Post


def registerPage(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            first_name = form.cleaned_data.get('first_name')
            last_name = form.cleaned_data.get('last_name')
            messages.success(request, f"Account created for {first_name} {last_name}!")
            return redirect('USERS-login')
    else:
        form = UserRegisterForm()
    return render(request, "users/register.html", {'form': form})


def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('USERS-dashboard')
        else:
            messages.warning(request, 'username or password is incorrect')

    context = {}
    return render(request, 'users/login.html', context)

@login_required
def dashboard(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, "users/dashboard.html", context)

