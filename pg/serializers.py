from rest_framework import serializers,routers
from .models import *

class pgdataSerializer(serializers.ModelSerializer):
    class Meta:
        model=pgdata
        fields='__all__'

class customerdataSerializer(serializers.ModelSerializer):
    class Meta:
        model=customerdata
        fields='__all__'
