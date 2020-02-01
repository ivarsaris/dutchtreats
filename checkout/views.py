from django.shortcuts import render
from django.contrib.auth.decorators import login_required
import stripe


# Create your views here.
stripe_api_key = settings.STRIPE_SECRET

@login_required()
