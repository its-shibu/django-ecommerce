from django import forms
from django.forms import ModelForm
from . models import Order


class OrderForm(ModelForm):
    class Meta:
        model = Order
        fields = ['product', 'quantity', 'payment', 'contact_no', 'address']
        widgets = {
            'product': forms.Select(attrs={'class': 'form-control'}),
            'quantity': forms.NumberInput(attrs={'class': 'form-control'}),
            'payment': forms.Select(attrs={'class': 'form-control'}),
            'contact_no': forms.TextInput(attrs={'class': 'form-control'}),
            'address': forms.Textarea(attrs={'class': 'form-control'}),
        }