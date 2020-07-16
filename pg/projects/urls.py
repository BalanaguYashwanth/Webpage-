"""main URL Configuration

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
from django.urls import path,include
from django.conf.urls import url
from filex.api import *
from filex import api
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    #path('',include('file.urls')),
    #path('',include('filex.urls')),
    path('',include('projects.urls')),

    path('acccounts/',include('acccounts.urls')),
    url(r'^api/v1/detailed/$',(api.detailed.as_view()),name='detailed'),
    url(r'^api/v1/Moredetail/(?P<id>\d+)/$',api.Moredetail.as_view(),name='Moredetail'),
    url(r'^api/v1/orderdetailed/$',(api.orderdetailed.as_view()),name='orderdetailed'),
    url(r'^api/v1/orderMoredetail/(?P<id>\d+)/$',api.orderMoredetail.as_view(),name='orderMoredetail'),

    url(r'^api/v1/filesdatadetailed/$',api.filesdatadetailed.as_view(),name='filesdatadetailed'),
    url(r'^api/v1/filesdataMoredetail/(?P<id>\d+)/$',api.filesdataMoredetail.as_view(),name='filesdataMoredetail'),


    url(r'^api/v1/slidedatadetailed/$',api.slidedatadetailed.as_view(),name='slidedatadetailed'),
    url(r'^api/v1/slidedataMoredetail/(?P<id>\d+)/$',api.slidedataMoredetail.as_view(),name='slidedataMoredetail'),
]

urlpatterns=urlpatterns+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)