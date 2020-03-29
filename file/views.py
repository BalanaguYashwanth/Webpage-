from django.shortcuts import render,redirect
from .models import upload
import zipfile,os, tempfile
from django.forms import modelformset_factory
from .forms import uploadForm
from rest_framework.views import APIView
from .serializers import *
from rest_framework.response import Response 

# Create your views here.
def home(request):
    if request.method=="POST":
        user=request.POST['user'];
        image=request.FILES['image'];
        upload.objects.create(user=user,image=image)
        files=upload.objects.all();
        return redirect('foundation')
    else:
        return render(request,'image.html')

def foundation(request):
    files=upload.objects.all();
    return render(request,'foundation.html',{'files':files})


class datalist(APIView):
    def get(self,request):
        datas=upload.objects.all()
        serializer = uploadSerializers(datas,many=True)
        return Response(serializer.data)
