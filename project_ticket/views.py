from django.shortcuts import render
from user_auth.forms import LogIn, CreateUser
from user_auth.models import MyUser
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

    return render(request, 'project_ticket/login.html', {'form': form})

@login_required(login_url='login')
def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('home'))

def home(request):
	return render(request, 'project_ticket/index.html', {'user': request.user})

@login_required(login_url='login')
def profile(request):
    return render(request, 'project_ticket/profile.html', {'user': request.user})

def register(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect(reverse('profile'))

    if request.method == 'GET':
       form = CreateUser()
    else:
        form = CreateUser(request.POST)
        if form.is_valid():
            user = MyUser()
            user.email = form.cleaned_data['email']
            user.first_name = form.cleaned_data['first_name']
            user.last_name = form.cleaned_data['last_name']
            if form.cleaned_data['password'] == form.cleaned_data['password_confirmation']:
                user.set_password(form.cleaned_data['password'])
                user.save()
                user = authenticate(username=form.cleaned_data['email'],
                                password=form.cleaned_data['password'])
                login(request, user)
                return HttpResponseRedirect(reverse('profile'))


    return render(request, 'project_ticket/register.html', { 'form':form, 'user': request.user })