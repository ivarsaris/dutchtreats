from django.shortcuts import render, redirect, reverse
from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from accounts.forms import UserLoginform, UserRegistrationForm


def index(request):
    """return index.html"""

    return render(request,
                'index.html')


@login_required
def logout(request):
    """log out user"""

    auth.logout(request)
    messages.success(request, "You have successfully logged out.")
    return redirect(reverse('index'))


def login(request):
    """return login page"""

    if request.user.is_authenticated:
        return redirect(reverse('index'))

    if request.method == "POST":
        login_form = UserLoginform(request.POST)

        if login_form.is_valid():
            user = auth.authenticate(username=request.POST['username'],
                                    password=request.POST['password'])

            if user:
                auth.login(user=user, request=request)
                messages.success(request, "You have successfully logged in.")
                return redirect(reverse('index'))

            else:
                login_form.add_error(None, "the username or password provided is incorrect.")

    else:
        login_form = UserLoginform()

    return render(request,
                'login.html',
                {'login_form': login_form})


def registration(request):
    """return registration page"""

    if request.user.is_authenticated:
        return redirect(reverse('index'))

    if request.method == 'POST':
        registration_form = UserRegistrationForm(request.POST)

        if registration_form.is_valid():
            registration_form.save()

            user = auth.authenticate(username=request.POST['username'],
                                    password=request.POST['password1'])

            if user:
                auth.login(user=user, request=request)
                messages.success(request, "Your registration was successful.")
                return redirect(reverse('index'))

            else:
                messages.error(request, "Registration failed, please try again.")

    else:
        registration_form = UserRegistrationForm()

    return render(request,
                 'registration.html',
                {'registration_form': registration_form})


def user_profile(request):
    """User profile page"""
    user = User.objects.get(email=request.user.email)
    return render(request,
                'profile.html',
                {'profile': user})
