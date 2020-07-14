from rest_framework import viewsets,routers,serializers
from .models import *
from .serializers import *

class pgdataViewsets(viewsets.ModelViewSet):
    queryset=pgdata.objects.all()
    serializer_class=pgdataSerializer


class customerdataViewsets(viewsets.ModelViewSet):
    queryset=customerdata.objects.all()
    serializer_class=customerdataSerializer



