from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from .forms import SignUpForm


def home(request):
    return render(request, 'master/index.html')


@login_required (login_url = '/login/')
def pos(request):
    return render(request,'pos.html')

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email')
            password1 = form.cleaned_data.get('password1')
            password2 = form.cleaned_data.get('password2')
            name = form.cleaned_data.get('name')
            contact_number = form.cleaned_data.get('contact_number')

            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})
