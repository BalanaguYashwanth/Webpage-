"""telsuko URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url
from todo.api import datalist,dataDetail 
from file import views
from rest_framework import routers
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework.routers import DefaultRouter,SimpleRouter
from file.viewsets import uploadViewsets
from iot.viewsets import showViewsets
from gate.viewsets import detailsViewset
from file.views import download




urlpatterns = [
    #path('accounts/',include('accounts.urls')),
    #url(r'^api/datalist/$',datalist.as_view(),name='datalist'),
    #url(r'^api/datalist/(?P<id>\d+)/$',dataDetail.as_view(),name='datalist'),
    
    #url(r'^file/$',views.datalist.as_view()),
    #url(r'^file/(?P<id>\d+)/$',views.datadetail.as_view()),
     url(r'^download/$',views.download.as_view()),

    
    #url(r'^file/$',views.datalist.as_view()),
    #url(r'^file/(?P<id>\d+)/$',views.datadetail.as_view()),
    
    #path('todo/',include('todo.urls')),
    #path('',include('calc.urls')),
    #path('',include('travel.urls')),
    #path('',include('todo.urls')),
    #path('',include('articles.urls')),
    
    path('',include('file.urls')),
    
    #path('',include('iot.urls')),
    
    path('admin/',admin.site.urls),
    #path('',include('gate.urls')),
  
    
    #path('api/v2/',include(router.urls)),
    #path('api/v1/',include(router.urls))

    
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns=format_suffix_patterns(urlpatterns)

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

