from rest_framework import viewsets
from .models import godryModel,outofstockModel,romobileModel,rolistModel,yv26Model,yv208Model,yv209dModel,empModel
from .serialaizer import empModelSerializer,godryModelSerializer,outofstockModelSerializer,romobileModelSerializer,\
    rolistModelSerializer,yv26ModelSerializer,yv208ModelSerializer,yv209dModelSerializer

class empModelViewset(viewsets.ModelViewSet):
    queryset = empModel.objects.all()
    serializer_class = empModelSerializer
class godryModelViewset(viewsets.ModelViewSet):
    queryset = godryModel.objects.all()
    serializer_class = godryModelSerializer
class outofstockModelViewset(viewsets.ModelViewSet):
    queryset = outofstockModel.objects.all()
    serializer_class = outofstockModelSerializer
class romobileModelViewset(viewsets.ModelViewSet):
    queryset = romobileModel.objects.all()
    serializer_class = romobileModelSerializer
class rolistModelViewset(viewsets.ModelViewSet):
    queryset = rolistModel.objects.all()
    serializer_class = rolistModelSerializer
class yv26ModelViewset(viewsets.ModelViewSet):
    queryset = yv26Model.objects.all()
    serializer_class = yv26ModelSerializer
class yv208ModelViewset(viewsets.ModelViewSet):
    queryset = yv208Model.objects.all()
    serializer_class = yv208ModelSerializer
class yv209dModelViewset(viewsets.ModelViewSet):
    queryset = yv209dModel.objects.all()
    serializer_class = yv209dModelSerializer


