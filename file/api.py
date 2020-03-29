from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import *
from .models import *

class datalist(APIView):
    def get(self,request):
        datas=upload.objects.all()
        serializer=uploadSerializers(datas,many=True)
        return Response(serializer.data)

    

