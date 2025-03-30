from .models import SpatialPoint, SpatialLineString, SpatialPolygon
from .exceptions import CustomAPIException
from .constants import *

# POINT
def create_point(data):
    if SpatialPoint.objects.filter(name=data['name']).exists():
        raise CustomAPIException(DUPLICATE_NAME, 409)
    try:
        return SpatialPoint.objects.create(**data)
    except Exception:
        raise CustomAPIException(INVALID_GEOMETRY, 400)

def get_point(id):
    try:
        return SpatialPoint.objects.get(id=id)
    except SpatialPoint.DoesNotExist:
        raise CustomAPIException(POINT_NOT_FOUND, 404)

# LINESTRING
def create_linestring(data):
    if SpatialLineString.objects.filter(name=data['name']).exists():
        raise CustomAPIException(DUPLICATE_NAME, 409)
    try:
        return SpatialLineString.objects.create(**data)
    except Exception:
        raise CustomAPIException(INVALID_GEOMETRY, 400)

def get_linestring(id):
    try:
        return SpatialLineString.objects.get(id=id)
    except SpatialLineString.DoesNotExist:
        raise CustomAPIException(LINESTRING_NOT_FOUND, 404)

# POLYGON
def create_polygon(data):
    if SpatialPolygon.objects.filter(name=data['name']).exists():
        raise CustomAPIException(DUPLICATE_NAME, 409)
    try:
        return SpatialPolygon.objects.create(**data)
    except Exception:
        raise CustomAPIException(INVALID_GEOMETRY, 400)

def get_polygon(id):
    try:
        return SpatialPolygon.objects.get(id=id)
    except SpatialPolygon.DoesNotExist:
        raise CustomAPIException(POLYGON_NOT_FOUND, 404)
