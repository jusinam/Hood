from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth import login,authenticate
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from .forms import SignupForm, HoodForm
from .models import Neighbourhood, Profile

# Create your views here.

@login_required(login_url='/accounts/login')
def index(request):
    
    return render(request,'index.html')

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('index')
    else:
        form = SignupForm()
    return render(request, 'registration/registration_form.html', {'form': form})
def home(request):
    all_hoods = Neighbourhood.objects.all()
    all_hoods=all_hoods[::-1]
    context={
        'all_hoods':all_hoods
    }
    return render(request,'home.html',context)
def addhood(request):
    if request.method =="POST":
        form  = HoodForm(request.POST,request.FILES)
        if form.is_valid():
            hood = form.save(commit=False)
            hood.admin = request.user.profile
            hood.save()
            return redirect('index')
    else:
        form = HoodForm()
    return render(request,'new-hood.html',{'form':form})

def profile(request,username):

    return render(request,'registration/profile.html')

