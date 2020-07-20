from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages
from django.template import RequestContext
from django.middleware.csrf import get_token
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import update_session_auth_hash
from acccounts.models import *


@csrf_exempt
def base(request):
   # user=request.user
    pg=userprofile.objects.get(user=request.user)
    return render(request,'member.html',{'pg':pg})


@csrf_exempt
def register(request):
    if request.method=="POST":
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        username=request.POST['username']
        email=request.POST['email']
        password=request.POST['password']
        password1=request.POST['password1']
        pg_id=request.POST['pgopt']
       
        if password==password1:
            if User.objects.filter(username=username).exists():
                messages.info(request,'username taken exists')
                return redirect(register)
            elif User.objects.filter(email=email).exists():
                messages.info(request,"email taken exists")
                return redirect(register)
            else:
                user=User.objects.create_user(first_name=first_name,last_name=last_name,username=username,email=email,password=password)
                user.save()
                userprofile.objects.create(pg_id=pg_id,user=user)
                return render(request,"loginform.html")
        else:
            messages.info(request," password and confirm password are not matching")
            return redirect(register)
    else:
        return render(request,'register.html')  

@csrf_exempt
def login(request):
    if request.method=='POST':
        
        username=request.POST['username']
        password=request.POST['password']


        user=auth.authenticate(username=username,password=password)

        #form = PasswordChangeForm(user=request.user, data=request.POST)
        # if request.user.is_authenticated:
        #     return render(request,'/loginforms.html')
        # else:
        #     return render(request,'loginform.html')

        #if request.session.has_key('username'):
        #    username = request.session['username']

        if user is not None:
            auth.login(request,user)
            # update_session_auth_hash(request, user.username)
            # request.session['user'] = request.POST['username']
            return redirect('base')
        else:
             messages.info(request,"Invalid Login Username & Password")
             return render(request,'loginform.html') 

    else:
        return render(request,'loginform.html')

# def process(request):
#     if request.session.has_key('user'):
#         #print(request.session.get("user"))
#         return redirect('/forms')
#     else:
#         messages.info(request,"Invalid Login Username & Password")
#         return render(request,'loginform.html') 


def logout(request):
    #del request.session['user']
    auth.logout(request)
    return redirect(login)



def your_view(request):
    csrf_token = get_token(request)
    csrf_token_html = '<input type="hidden" name="csrfmiddlewaretoken" value="{}" />'.format(csrf_token)