from django.contrib.auth import login  , authenticate
from django.shortcuts import render
from django.http import HttpResponseRedirect

from django.contrib.auth.decorators import login_required
...

def login(request):
    if request.method == 'GET':
        _username = request.POST['username']
        _password = request.POST['password']
        user = authenticate(username=_username, password=_password)
        if user is not None and user. is_admin:
            login(request, user)
            return HttpResponseRedirect(request.GET.get('dash'))
        else:
            return  HttpResponseRedirect(request.GET.get('super'))
    else:
         return render(request, 'login.html')

...
@login_required (login_url = '/login/')
def dash(request):
    if request.user.is_authenticated():
        return render(request, 'master/index.html')
    else:
        return redirect('super')


@login_required (login_url = '/login/')
def super(request):
    if request.user.is_authenticated():
        return render(request, 'admin.html')
    else:
        return redirect('super')
