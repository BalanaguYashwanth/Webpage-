from django.shortcuts import render,redirect
from .models import *

def home(request):
    return render(request,'member.html')


def all(request):
    return render(request,'all.html')

def firstpage(request):
    if request.method=="POST":
        pgname=request.POST["pgname"]
        location=request.POST["location"]
        pgdata.objects.create(pgname=pgname,location=location)
        all=pgdata.objects.all()
        return render(request,"firstpage.html",{"all":all})
    else:
        all=pgdata.objects.all()
        return  render(request,'middlepage.html',{"all":all})

    

