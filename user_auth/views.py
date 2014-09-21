from django.shortcuts import render
from user_auth.forms import LogIn
from django.contrib.auth.decorators import login_required

def login(request):

    if request.method == 'GET':
        form = LogIn()
    else:
        form = LogIn(request.POST)
        if form.is_valid():
            user = authenticate(username=request.POST['email'],
                                password=request.POST['password'])
            login(request, user)

            return HttpResponseRedirect(reverse('home'))

    return render(request, 'user_auth/login.html', {'form': form})

@login_required(login_url='login')
def home(request):
	return render(request, 'user_auth/index.html')