from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
    return render(request, 'accounts/login.html')

# def logout_view(request):
#    return render(request, 'accounts/logout.html')

def signup_view(request):
    return render(request, 'accounts/signup.html')

# Create your views here.
