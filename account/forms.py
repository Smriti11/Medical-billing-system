from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from medi.models import MyUser

class SignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=255,required=True)
    contact_number = forms.IntegerField(required=True)
    name = forms.CharField(max_length=255,required=True)

    class Meta:
        model = MyUser
        fields = ("email", "contact_number", "name", "password1", "password2")

    def save(self, commit=True):
        user = super(UserCreationForm, self).save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user
