from django import forms
from .models import Stockreturn

class AddStockreturnForm(forms.ModelForm):
    class Meta:
        model = Stockreturn
        fields = '__all__'
