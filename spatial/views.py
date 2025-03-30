from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import *
from .services import *
from .constants import SUCCESS_CREATE, SUCCESS_FETCH

def api_response(success, message, data=None):
    return {"success": success, "message": message, "data": data}

# POINT
class CreatePointView(APIView):
    def post(self, request):
        point = create_point(request.data)
        serialized = SpatialPointSerializer(point).data
        return Response(api_response(True, SUCCESS_CREATE, serialized), status=status.HTTP_201_CREATED)

class RetrievePointView(APIView):
    def get(self, request, id):
        point = get_point(id)
        serialized = SpatialPointSerializer(point).data
        return Response(api_response(True, SUCCESS_FETCH, serialized), status=status.HTTP_200_OK)

# LINESTRING
class CreateLineView(APIView):
    def post(self, request):
        line = create_linestring(request.data)
        serialized = SpatialLineStringSerializer(line).data
        return Response(api_response(True, SUCCESS_CREATE, serialized), status=status.HTTP_201_CREATED)

class RetrieveLineView(APIView):
    def get(self, request, id):
        line = get_linestring(id)
        serialized = SpatialLineStringSerializer(line).data
        return Response(api_response(True, SUCCESS_FETCH, serialized), status=status.HTTP_200_OK)

# POLYGON
class CreatePolygonView(APIView):
    def post(self, request):
        polygon = create_polygon(request.data)
        serialized = SpatialPolygonSerializer(polygon).data
        return Response(api_response(True, SUCCESS_CREATE, serialized), status=status.HTTP_201_CREATED)

class RetrievePolygonView(APIView):
    def get(self, request, id):
        polygon = get_polygon(id)
        serialized = SpatialPolygonSerializer(polygon).data
        return Response(api_response(True, SUCCESS_FETCH, serialized), status=status.HTTP_200_OK)
