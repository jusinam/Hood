from django.shortcuts import render,redirect,get_object_or_404


# Create your views here.

@login_required(login_url='/accounts/login')
def index(request):
   
    return render(request,'index.html')


