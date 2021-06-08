from .viewsets import yqlabModelViewset,yvrokarModelViewset
from rest_framework import routers

router=routers.DefaultRouter()
router.register('yqlab',yqlabModelViewset)
router.register('yvrokar',yvrokarModelViewset)
