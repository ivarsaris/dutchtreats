from django.shortcuts import render, redirect, reverse
from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .forms import UserLoginform, UserRegistrationForm, UserUpdateForm, ProfileUpdateForm


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

        """save user's username and password to database"""
        if login_form.is_valid():
            user = auth.authenticate(username=request.POST['username'],
                                    password=request.POST['password'])

            """successfull login redirects to homepage and displays successfull login message"""
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

            """save users username and password to database"""
            user = auth.authenticate(username=request.POST['username'],
                                    password=request.POST['password1'])

            """
            redirect to homepage and give message that
            registration was successful
            """
            if user:
                auth.login(user=user, request=request)
                messages.success(request, "Your registration was successful.")
                return redirect("/")

            else:
                messages.error(request, "Registration failed, please try again.")

    else:
        registration_form = UserRegistrationForm()

    return render(request,
                 'registration.html',
                {'registration_form': registration_form})


def user_profile(request):
    """User profile page. if user is not logged in, they're redirected 
    to login page with message. Else, they're profile is opened"""

    if request.user.is_anonymous:
        messages.add_message(request, messages.INFO,
                             'You must be logged in to visit your profile.')
        return redirect('login')
    else:
        user = User.objects.get(email=request.user.email)

        if request.method == 'POST':

            """post forms if new data is given"""
            UserUpdate_Form = UserUpdateForm(request.POST, instance=request.user)
            ProfileUpdate_Form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)

            """check if both forms are valid"""
            if UserUpdate_Form.is_valid() and ProfileUpdate_Form.is_valid():
                
                """update user and profile"""
                UserUpdate_Form.save()
                ProfileUpdate_Form.save()

                messages.success(request, "Your profile has been updated!")
                return redirect('profile')

        else:
            
            """keep data as is if no new data is given"""
            UserUpdate_Form = UserUpdateForm(instance=request.user)
            ProfileUpdate_Form = ProfileUpdateForm(instance=request.user.profile)

        return render(request,
                    'profile.html',
                    {
                    'profile': user,
                    'UserUpdate_Form': UserUpdate_Form,
                    'ProfileUpdate_Form': ProfileUpdate_Form}
                    )
