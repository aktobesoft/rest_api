from django.contrib import admin
from django.urls import path, include
from .views import PedigreeViewSet

from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'pedigree', PedigreeViewSet)

urlpatterns = [
     path('', include(router.urls)),
]