
from rest_framework import routers
from file.viewsets import  uploadViewsets
from rest_framework.routers import DefaultRouter

router = routers.DefaultRouter()
router.register('upload',uploadViewsets)
