from django import forms
from .models import Order

# class MakePaymentForm(forms.Form):

#     MONTH_CHOICES = [(i, i) for i in range(1, 12)]
#     YEAR_CHOICES = [(i, i) for i in range(2020, 2039)]

#     credit_card_number = forms.CharField(label='Credit card number', required=False)
#     cvv = forms.CharField(label='Security code (CVV)', required=False)
#     expiry_month = forms.ChoiceField(label='Expiry month', choices=MONTH_CHOICES, required=False)
#     expiry_year = forms.ChoiceField(label='Expiry year', choices=YEAR_CHOICES, required=False)
#     stripe_id = forms.CharField(widget=forms.HiddenInput)

"""get all neccessary information for payment with stripe credit card"""
class MakePaymentForm(forms.Form):

    MONTH_CHOICES = [(i, i) for i in range(1, 12)]
    YEAR_CHOICES = [(i, i) for i in range(2020, 2039)]

    credit_card_number = forms.CharField(label='Credit card number. Stripe credit card test number is 4242424242424242',
                                         max_length=16, min_length=16,
                                         required=False)
    cvv = forms.CharField(label='Security code (CVV)',
                          max_length=3, min_length=3,
                          required=False)
    expiry_month = forms.ChoiceField(label='Expiry month',
                                     choices=MONTH_CHOICES,
                                     required=False)
    expiry_year = forms.ChoiceField(label='Expiry year',
                                    choices=YEAR_CHOICES,
                                    required=False)
    stripe_id = forms.CharField(widget=forms.HiddenInput)

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ('full_name', 'phone_number', 'country', 'postal_code', 
        'street_address1', 'street_address2', 'province')

