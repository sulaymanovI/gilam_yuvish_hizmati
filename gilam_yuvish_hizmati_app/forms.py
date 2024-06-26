from django import forms
from .models import Buyurtma
import re
from django.core.validators import RegexValidator


class BuyurtmaForm(forms.ModelForm):
    telefon_raqam=forms.CharField(max_length=13 , min_length=9)
    class Meta:
        model=Buyurtma
        fields=['fullname','telefon_raqam','hizmat_turi','manzil']
