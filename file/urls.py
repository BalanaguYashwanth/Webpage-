from django.contrib import admin 
from django.urls import path,include
from django.conf import settings 
from django.conf.urls.static import static 
from . views import *
from rest_framework import routers
from rest_framework.routers import DefaultRouter,SimpleRouter
from .viewsets import uploadViewsets

router = routers.SimpleRouter()
router.register('upload',uploadViewsets,basename="upload")

urlpatterns=[
    path('',home,name= "home"),
    #path(r'^download/(?P<id>\d+)/$',download.as_view(),name="download"),
    path('foundation',foundation,name="foundation"),
    path('api/v1/',include(router.urls))
]




