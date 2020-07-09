from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(details)
admin.site.register(orderdetails)
admin.site.register(filesdata)