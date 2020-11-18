from rest_framework import serializers
from .models import Pedigree

class PedigreeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Pedigree
        fields = "__all__"