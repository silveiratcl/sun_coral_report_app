"""
URL mappings for the marker app.
"""
from django.urls import(
    path,
    include,
)
from rest_framework.routers import DefaultRouter

from markers import views
from markers.views import MarkersMapView

router = DefaultRouter()
router.register('markers', views.MarkerViewSet)

app_name = 'markers'

urlpatterns = [
    path('', include(router.urls)),
    path('map/', MarkersMapView.as_view()),
]
