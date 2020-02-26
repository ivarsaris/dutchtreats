from django.forms import ModelForm, TextInput
from .models import Review
from django import forms


class ReviewForm(forms.ModelForm):
    """
    form for review that can be added to product
    """
    content = forms.CharField(
    label='Write your own review(you need to be logged in).',
    widget=forms.Textarea())

    class Meta:
        model = Review
        fields = ['content']
