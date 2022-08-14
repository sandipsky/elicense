from multiprocessing import context
from django.shortcuts import render, redirect
from .models import *
from .forms import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

# Create your views here.

def index(request):
    return render(request, 'index.html')

def contact(request):
    return render(request, 'contact.html')

def about(request):
    return render(request, 'aboutus.html')

@login_required(login_url='login')
def apply(request):
    applied = License.objects.filter(applicant=request.user).count()
    if applied > 0:
        return render(request, "wait.html")
    else:
        if request.method == 'POST':
            aform = ApplicantForm(request.POST, files=request.FILES)
            lform = LicenseForm(request.POST, files=request.FILES)
            lform.instance.applicant = request.user
            if aform.is_valid() and lform.is_valid(): 
                aform.instance.user = request.user
                lform.instance.applicant = request.user
                aform.save()
                lform.save()
                return redirect("index")
        else: 
            aform = ApplicantForm()
            lform = LicenseForm()
        return render(request, "apply.html", {'aform':aform, 'lform':lform})

def loginuser(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')
    return render(request, 'login.html')

def register(request):
    form = CreateUser(request.POST)
    if request.method == 'POST':
        form = CreateUser(request.POST)
        if form.is_valid():
            new_user = form.save(commit=False)
            new_user.save()
            return redirect('login')
    else:
        form = CreateUser()
    context = {
        'form' : form
    }
    return render(request, 'register.html', context)

@login_required(login_url='login')
def logoutuser(request):
    logout(request)
    return redirect('login')

@login_required(login_url='login')
def dashboard(request):
    applied = License.objects.filter(applicant=request.user).count()
    return render(request, 'dashboard.html', {'applied':applied})

@login_required(login_url='login')
def detail(request):
    license = License.objects.get(applicant=request.user)
    applicant = ApplicantInfo.objects.get(user=request.user)
    
    context = {
        'lform' : license,
        'aform' : applicant,

    }
    return render(request, 'detail.html', context)