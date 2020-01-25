from django import forms

class UserLoginform(forms.Form):
    """form for user to log in"""
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)