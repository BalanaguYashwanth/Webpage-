from rest_framework import viewsets
from .import serializers
from file.models import upload
from .serializers import uploadSerializers

class uploadViewsets(viewsets.ModelViewSet):
    queryset = upload.objects.all()
    serializer_class = uploadSerializers 

