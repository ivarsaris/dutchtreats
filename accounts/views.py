from django.shortcuts import render, redirect, reverse
from django.contrib import auth, messages

def index(request):
    """return index.html"""
    return render(request, 'index.html')

def logout(request):
    """log out user"""
    auth.logout(request)
    messages.success(request, "You have successfully logged out.")
    return redirect(reverse('index'))

def login(request):
    """return login page"""
    return render(request, 'login.html')