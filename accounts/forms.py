from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError
from .models import Profile


class UserLoginform(forms.Form):
    """form for user to log in"""

    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'style': 'border: 2px solid black; border-radius: 4px;'
        }
    )
)

    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'style': 'border: 2px solid black; border-radius: 4px;'
        }
    )
)


class UserRegistrationForm(UserCreationForm):
    """form to register a new user"""

    email = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'style': 'border: 2px solid black; border-radius: 4px;'
        }
    )
)

    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'style': 'border: 2px solid black; border-radius: 4px;'
        }
    )
)

    password1 = forms.CharField(label="Password",
                                widget=forms.PasswordInput(
                                    attrs={
                'style': 'border: 2px solid black; border-radius: 4px;'
        }
    )
)
    password2 = forms.CharField(label="Confirm password",
                                widget=forms.PasswordInput(
                                    attrs={
                'style': 'border: 2px solid black; border-radius: 4px;'
        }
    )
)
    class Meta:
        model = User
        fields = ['email', 'username', 'password1', 'password2']

    def clean_email(self):
        email = self.cleaned_data.get('email')
        username = self.cleaned_data.get('username')
        if User.objects.filter(email=email).exclude(username=username):
            raise forms.ValidationError('Account with this Email address already exists.')
        return email

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')

        if not password1 or not password2:
            raise ValidationError("Please confirm your password.")

        if password1 != password2:
            raise ValidationError("Passwords must match.")

        return password2

class UserUpdateForm(forms.ModelForm):
    """form for user to update their profile"""
    email = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'style': 'border: 2px solid black; border-radius: 4px;'
        }
    )
)

    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'style': 'border: 2px solid black; border-radius: 4px;'
        }
    )
)

    class Meta:
        model = User
        fields = ['email', 'username']

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']
