from django.shortcuts import render

def home(request):
    return render(request, 'home.html', {})

def login(request):
    return render(request, 'registration/login.html', {})

def logout(request):
    pass

def gig_detail(request, id):
    return render(request, 'gig_detail.html', {})
