from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.
def home(request):
    return render(request,'html/home.html')

@login_required
def computer(request):
    return render(request,'html/computer.html')

@login_required
def mobile(request):
    return render(request,'html/mobile.html')

@login_required
def pendrive(request):
    return render(request,'html/pendrive.html')


def logout(request):
    return render(request,'html/logout.html')
