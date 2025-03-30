from django.urls import path
from .views import (
    CreatePointView, RetrievePointView,
    CreateLineView, RetrieveLineView,
    CreatePolygonView, RetrievePolygonView
)

urlpatterns = [
    # POINT
    path('points/', CreatePointView.as_view(), name='create_point'),
    path('points/<int:id>/', RetrievePointView.as_view(), name='get_point'),

    # LINE
    path('lines/', CreateLineView.as_view(), name='create_line'),
    path('lines/<int:id>/', RetrieveLineView.as_view(), name='get_line'),

    # POLYGON
    path('polygons/', CreatePolygonView.as_view(), name='create_polygon'),
    path('polygons/<int:id>/', RetrievePolygonView.as_view(), name='get_polygon'),
]
