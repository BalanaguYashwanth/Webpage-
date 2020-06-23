from rest_framework import serializers
from .models import *

class detailsSerializer(serializers.ModelSerializer):
    class Meta:
        model=details
        fields='__all__'

class orderdetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model=orderdetails
        fields='__all__'
    