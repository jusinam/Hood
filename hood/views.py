from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth import login,authenticate
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from .forms import SignupForm, HoodForm, BusinessForm, PostForm, UpdateProfileForm
from .models import Neighbourhood, Profile, Business, Post

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

def unohood(request,id):
    hood = Neighbourhood.objects.get(id = id)
    buss = Business.objects.filter(neighbourhood=hood)
    posts = Post.objects.filter(hood=hood)
    posts = posts[::-1]
    if request.method == "POST":
        form = BusinessForm(request.POST)
        if form.is_valid():
            busin_form = form.save(commit=False)
            busin_form.neighbourhood = hood
            busin_form.user = request.user.profile
            busin_form.save()
            return redirect('unhood', hood.id)
    else:
        form = BusinessForm()
    context ={
        'hood':hood,
        'business':buss,
        'posts':posts,
        'form':form,      
    }
    return render(request,'hood.html',context)

def hoodneighbours(request, hood_id):
    hood = Neighbourhood.objects.get(id=hood_id)
    neighbours = Profile.objects.filter(neighbourhood = hood)
    return render(request,'neighbours.html',{'neighbours':neighbours})

def addpost(request,hood_id):
    hood = Neighbourhood.objects.get(id=hood_id)
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.hood =hood
            post.user = request.user.profile
            post.save()
            return redirect('unhood',hood.id)
    else:
        form =PostForm
    return render(request,'post.html',{'form':form})

def joinhood(request,id):
    neighbourhood = get_object_or_404(Neighbourhood,id=id)
    request.user.profile.neighbourhood=neighbourhood
    request.user.profile.save()
    return redirect('hood')

def leavehood(request,id):
    hood = get_object_or_404(Neighbourhood,id=id)
    request.user.profile.neighbourhood=None
    request.user.profile.save()
    return redirect('hood')

