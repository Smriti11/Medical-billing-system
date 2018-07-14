from django import forms
from .models import Purchase

class AddPurchaseForm(forms.ModelForm):
    class Meta:
        model = Purchase
        fields = '__all__'
