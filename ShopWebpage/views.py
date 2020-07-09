from django.shortcuts import render,redirect
from .models import details
from filex.models import orderdetails
from filex.models import *
from django.contrib.auth.decorators import login_required
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from django.middleware.csrf import get_token
from django.views.decorators.csrf import csrf_exempt


# Create your views here.
@csrf_exempt
def home(request):
    return render(request,'main.html')


@login_required(login_url='acccounts/login') 
def forms(request):
    return render(request,'forms.html')
    
@login_required(login_url='acccounts/login') 
def imageforms(request):
    return render(request,'imageforms.html')

@login_required(login_url='acccounts/login') 
def postimage(request):
    return render(request,'postimage.html')

@login_required(login_url='acccounts/login') 
def slidepostimage(request):
    return render(request,'slidepostimage.html')

@login_required(login_url='acccounts/login') 
def secondaryimages(request):
    return render(request,'secondaryimages.html')

@login_required(login_url='acccounts/login')
def primaryimages(request):
    return render(request,'primaryimages.html')

@login_required(login_url='acccounts/login')
def slideimage(request):
    return render(request,'fileimages.html')

@login_required(login_url='acccounts/login')
def slideimages(request):
    return render(request,'slideimages.html')

@login_required(login_url='acccounts/login')
def images(request):
    return render(request,'images.html')

@login_required(login_url='acccounts/login')
def contactdatas(request):
    return render(request,'contactdatas.html')

@login_required(login_url='acccounts/login')
def orderdatas(request):
    return render(request,"orderdatas.html")
