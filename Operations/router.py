from .viewsets import empModelViewset
from rest_framework import routers

router=routers.DefaultRouter()
router.register('emp',empModelViewset)