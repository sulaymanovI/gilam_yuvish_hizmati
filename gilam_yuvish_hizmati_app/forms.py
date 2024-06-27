from django import forms
from .models import Buyurtma

class BuyurtmaForm(forms.ModelForm):
    telefon_raqam=forms.CharField(max_length=13 , min_length=9)
    class Meta:
        model=Buyurtma
        fields=['fullname','telefon_raqam','hizmat_turi','manzil']

    def __init__(self,*args, **kwargs):
        super(BuyurtmaForm , self).__init__(*args, **kwargs)
        self.fields['manzil'].label="Manzil (Ixtiyoriy)" 