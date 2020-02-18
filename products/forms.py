from django.forms import ModelForm, TextInput
from .models import Review
from django import forms


class ReviewForm(forms.ModelForm):
    """
    form for review that can be added to product
    """
    content = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Content'}))

    class Meta:
        model = Review
        fields = ['content']
