from user_auth.forms import LogIn, CreateUser
from project_ticket.forms import EditInfo, EditPassword
from user_auth.models import MyUser
from project_ticket.models import Project
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.shortcuts import render, get_object_or_404


def login_view(request):
    """
    If the request method is post then the user 
    will be authenticated and if authenticated
    correctly they will be redirected to the 
    profile page.
    """
    if request.user.is_authenticated():
        return HttpResponseRedirect(reverse('profile'))

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
    """
    The tag above is an attribute tag that states 
    that a user must be logged into accesss this URL.
    A user must obviously be logged in to log out.
    Utlizing the Django logout function and then
    redirecting afterwards the users will be
    redirected to the home page.
    """
    logout(request)
    return HttpResponseRedirect(reverse('home'))

def home(request):
    return render(request, 'project_ticket/landing.html', {'user': request.user})

@login_required(login_url='login')
def profile(request):
    """
    Each user will need different query sets based
    on the type of user they are. So based on the 
    user types we run a query which will get all
    projects that they are related to.
    """
    user = request.user

    if user.perm == "developer":
        user_projects = Project.objects.filter(developer=user)
    elif user.perm == "client":
        user_projects = Project.objects.filter(client=user)
    elif user.perm == "project_manager":
        user_projects = Project.objects.filter(project_manager=user)
    else:
        user_projects = []

    return render(request, 'project_ticket/profile.html', {'user': user, 'projects': user_projects })

@login_required(login_url='login')
def project(request, project_id):
    """
    This view is passed in a project_id from the URL
    using a regular expression that matches any number.
    This number is extracted and used to match a project.
    Although the user needs to be related in some way to 
    the project in the ORM to actually be allowed to view it.
    """
    user = request.user
    project = get_object_or_404(Project, id=project_id)

    is_related_dev = False
    is_related_pm = False
    # Users should not be able to view projects they are not related too
    if user.perm == "developer":
        for dev in project.developer.all():
            if user.email == dev.email:
                is_related_dev = True
        if is_related_dev == False:
          return HttpResponseRedirect(reverse('profile'))  

    elif user.perm == "client":
        if project.client != user:
            return HttpResponseRedirect(reverse('profile'))

    elif user.perm == "project_manager":
        for proj_man in project.project_manager.all():
            if user.email == proj_man.email:
                is_related_pm = True
        if is_related_pm == False:
            return HttpResponseRedirect(reverse('profile'))
    
    else:
        return HttpResponseRedirect(reverse('profile'))

    all_tickets = project.tickets.all()

    return render(request, 'project_ticket/project.html', {'project':project, 'tickets': all_tickets })



@login_required(login_url='login')
def editprofile(request):
    user = request.user
    if request.method == 'POST':
        form = EditInfo(request.POST)
        form2 = EditPassword(request.POST, empty_permitted=True)
        if form.is_valid() and form2.is_valid() and form2.has_changed():
            if user.check_password(form2.cleaned_data['old_password']):
                if form2.cleaned_data['new_password'] == form2.cleaned_data['confirm_password']:
                    user.first_name = form.cleaned_data['firstname']
                    user.last_name = form.cleaned_data['lastname']
                    user.email = form.cleaned_data['email']
                    user.set_password(form2.cleaned_data['new_password'])
                    user.save()

        elif form.is_valid() and not(form2.has_changed()):
                user.first_name = form.cleaned_data['firstname']
                user.last_name = form.cleaned_data['lastname']
                user.email = form.cleaned_data['email']
                user.save()

    else:
        form = EditInfo(
                    initial={ 'firstname': user.first_name,
                            'lastname': user.last_name,
                            'email' : user.email,
                            }
                    )
        form2 = EditPassword()

    return render(request, 'project_ticket/editprofile.html', {'form':form, 'form2':form2, 'user': request.user})



def register(request):
    """
    If the request method is post then a MyUser object 
    will be created with a the desired info from the 
    HTML forms. The user will then authenticate and
    be redirected to the profile page.
    """
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
