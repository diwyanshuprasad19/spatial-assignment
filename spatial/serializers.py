from rest_framework import serializers
from .models import SpatialPoint, SpatialLineString, SpatialPolygon

class SpatialPointSerializer(serializers.ModelSerializer):
    class Meta:
        model = SpatialPoint
        fields = ['id', 'name', 'location']

class SpatialLineStringSerializer(serializers.ModelSerializer):
    class Meta:
        model = SpatialLineString
        fields = ['id', 'name', 'path']

class SpatialPolygonSerializer(serializers.ModelSerializer):
    class Meta:
        model = SpatialPolygon
        fields = ['id', 'name', 'area']
