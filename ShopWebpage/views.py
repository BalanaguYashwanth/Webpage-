from django.shortcuts import render,redirect
from .models import details
from filex.models import orderdetails

# Create your views here.
def home(request):
    return render(request,'main.html')

def update(request,id):
    return render(request,'update.html',{'id1':id})

def data(request):
    if request.method=="POST":
        person=request.POST['person']
        place=request.POST['place']
        phone=request.POST['phone']
        email=request.POST['email']
        details.objects.create(phone=phone,email=email,place=place,person=person)
        all=details.objects.all()
        return redirect(home)
    else:
        return render(request,'filex.html')


def order(request):
    if request.method=="POST":
        name=request.POST['name']
        item=request.POST['item']
        time=request.POST['time']
        orderdetails.objects.create(name=name,time=time,item=item)
        collect=orderdetails.objects.all()
        return redirect(home)
    else:
        return render(request,"filey.html")
    
# def alldata(request):
#     return redirect(request,"filex.html")
