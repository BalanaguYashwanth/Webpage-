from rest_framework import routers, serializers, viewsets

from .models import upload

class uploadSerializers(serializers.ModelSerializer):
    class Meta:
        model = upload
        fields = '__all__'

