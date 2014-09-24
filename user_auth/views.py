from django.shortcuts import render
from user_auth.forms import LogIn
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

def login_view(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect(reverse('home'))

    if request.method == 'GET':
        form = LogIn()
    else:
        form = LogIn(request.POST)
        if form.is_valid():
            user = authenticate(username=request.POST['email'],
                                password=request.POST['password'])
            login(request, user)

            return HttpResponseRedirect(reverse('profile'))

    return render(request, 'user_auth/login.html', {'form': form})

@login_required(login_url='login')
def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('home'))

def home(request):
	return render(request, 'user_auth/index.html', {'user': request.user})

@login_required(login_url='login')
def profile(request):
    return render(request, 'user_auth/profile.html', {'user': request.user})

