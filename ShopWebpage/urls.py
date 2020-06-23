from django.urls import path
from . import views

urlpatterns=[
    path('',views.home,name="home"),
    path('data',views.data,name="data"),
    path('order',views.order,name="order"),
    path('update/<str:id>/',views.update,name="update")
]

