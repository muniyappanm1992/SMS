from .viewsets import godryModelViewset,outofstockModelViewset,romobileModelViewset,rolistModelViewset,yv26ModelViewset,\
    yv208ModelViewset,yv209dModelViewset
from rest_framework import routers

router=routers.DefaultRouter()
router.register('godry',godryModelViewset)
router.register('outofstock',outofstockModelViewset)
router.register('romobile',romobileModelViewset)
router.register('rolist',rolistModelViewset)
router.register('yv26',yv26ModelViewset)
router.register('yv208',yv208ModelViewset)
router.register('yv209d',yv209dModelViewset)