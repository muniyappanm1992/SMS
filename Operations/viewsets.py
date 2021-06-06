from rest_framework import viewsets
from .models import empModel
from .serialaizer import empModelSerializer

class empModelViewset(viewsets.ModelViewSet):
    queryset = empModel.objects.all()
    serializer_class = empModelSerializer

