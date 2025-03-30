from django.contrib.gis.db import models

class SpatialPoint(models.Model):
    name = models.CharField(max_length=100, unique=True)
    location = models.PointField()

    def __str__(self):
        return self.name

class SpatialLineString(models.Model):
    name = models.CharField(max_length=100, unique=True)
    path = models.LineStringField()

    def __str__(self):
        return self.name

class SpatialPolygon(models.Model):
    name = models.CharField(max_length=100, unique=True)
    area = models.PolygonField()

    def __str__(self):
        return self.name
