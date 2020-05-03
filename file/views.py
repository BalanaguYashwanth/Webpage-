from django.shortcuts import render,redirect
from .models import upload
import zipfile as ZipFile
import os, tempfile
from django.forms import modelformset_factory
from .forms import uploadForm
from rest_framework.views import APIView
from .serializers import *
from rest_framework.response import Response 
from rest_framework import viewsets
from rest_framework import status
import zipfile
from django.views import View 
from .import serializers
from file.models import upload
from .serializers import uploadSerializers
import os 
from zipfile import ZIP_DEFLATED
from django_zipfile import TemplateZipFile
from django.shortcuts import get_list_or_404, get_object_or_404
from django.http import HttpResponse
from django.utils.encoding import smart_str
from wsgiref.util import FileWrapper #django >1.8
os.chdir("C:/Users/Admin/Desktop")
import io  
#import urllib2



def get_file_name(filePath):
    head, tail = os.path.split(filePath)
    return tail

def home(request):
    if request.method=="POST":
        user=request.POST['user'];
        image=request.FILES['image'];
        upload.objects.create(user=user,image=image)
        files=upload.objects.all();
        return redirect('foundation')
    else:
        return render(request,'file.html')

def foundation(request):
    files=upload.objects.all();
    return render(request,'foundation.html',{'files':files})

class download(APIView):

 def get(self,request):
    filenames = [r"C:\Users\Admin\projects\telsuko\im.jpg"]
    zip_subdir = "somefiles"
    zip_filename = "%s.zip" % zip_subdir
    s = io.BytesIO()

    zf = zipfile.ZipFile(s, "w")

    for fpath in filenames:
 
        fdir, fname = os.path.split(fpath)
        zip_path = os.path.join(zip_subdir, fname)
        zf.write(fpath, zip_path)
        zf.close()
    resp = HttpResponse(s.getvalue(), content_type = "application/x-zip-compressed")
    resp['Content-Disposition'] = 'attachment; filename=%s' % zip_filename
    return resp


class datalist(APIView):
    def get(self,request):
        datas=upload.objects.all()
        serializer = uploadSerializers(datas,many=True)
        return Response(serializer.data)

    def post(self,request):
        serializer=uploadSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    def delete(self,request):
        serializer=upload.objects.all()
        serializer.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class datadetail(APIView):
    def get(self,request,id):
        model=upload.objects.get(id=id)
        serializer=uploadSerializers(model)
        return Response(serializer.data)

    def delete(self,request,id):
        serializer=upload.objects.get(id=id)
        serializer.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    





