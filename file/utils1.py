
from zipfile import ZIP_DEFLATED
from django_zipfile import TemplateZipFile
from django.shortcuts import get_list_or_404, get_object_or_404
from django.http import HttpResponse
import zipfile
import os
from wsgiref.util import FileWrapper #django >1.8
from shutil import make_archive
import io  



def zip(complete_file_name):
    files_path = "C:/Users/Admin/projects/telsuko/media/photos/"
    path_to_zip = make_archive(files_path, "zip", files_path)
    response = HttpResponse(FileWrapper(open(path_to_zip,'rb')), content_type='application/zip')
    response['Content-Disposition'] = 'attachment; filename="{filename}.zip"'.format(
        filename = complete_file_name.replace(" ", "_")
    )
    return response
