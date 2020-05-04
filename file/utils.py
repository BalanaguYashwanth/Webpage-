


from zipfile import ZIP_DEFLATED
from django_zipfile import TemplateZipFile
from django.shortcuts import get_list_or_404, get_object_or_404
from django.http import HttpResponse
import zipfile
import os
from wsgiref.util import FileWrapper #django >1.8

import io  



def zip(complete_file_name):

    #link= r"C:\Users\Admin\projects\telsuko\media\photos\ "
    #link=link[:-1]+complete_file_name
    #filenames=os.path.normpath(link)
    filenames = [r"C:\Users\Admin\projects\telsuko\media\photos"]
    #filenames=filenames+complete_file_name
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
    return filenames
    
