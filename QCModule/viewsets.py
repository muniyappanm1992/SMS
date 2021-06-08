from rest_framework import viewsets
from .models import yqlabModel,yvrokarModel
from .serialaizer import yqlabModelSerializer,yvrokarModelSerializer

class yqlabModelViewset(viewsets.ModelViewSet):
    queryset = yqlabModel.objects.all()
    serializer_class = yqlabModelSerializer
class yvrokarModelViewset(viewsets.ModelViewSet):
    queryset = yvrokarModel.objects.all()
    serializer_class = yvrokarModelSerializer


