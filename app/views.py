from django.shortcuts import render


def home(request):
    return render(request, 'app/dashboard.html', {'title': "App title"})


def about(request):
    return render(request, 'app/about.html')
