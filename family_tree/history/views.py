from django.shortcuts import render
from django.http import JsonResponse
from .models import Pedigree

from rest_framework.decorators import api_view
from rest_framework import viewsets
from .serializers import PedigreeSerializer


#@api_view(['GET'])
class PedigreeViewSet(viewsets.ModelViewSet):
    queryset = Pedigree.objects.all()
    serializer_class = PedigreeSerializer