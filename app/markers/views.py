"""Markers API views."""
from rest_framework import viewsets
from rest_framework_gis import filters
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from django.contrib.gis.geos import Point
from django.views.generic.base import TemplateView


from core.models import Marker
from markers.serializers import MarkerSerializer


class MarkerViewSet(viewsets.ModelViewSet):
    """Marker view set."""

    bbox_filter_field = "location"
    filter_backends = (filters.InBBoxFilter,)
    queryset = Marker.objects.all()
    serializer_class = MarkerSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        """Retrieve markers for authenticated user"""
        return self.queryset.filter(user=self.request.user).order_by('-id')

    def get_serializer_class(self):
        """Return the serializer class for request"""
        if self.action == 'list':
            return serializer.MarkerSerializer

        return self.serializer_class

    def perform_create(self, serializer):
        """Create a new marker"""
        serializer.save(user=self.request.user)

class MarkersMapView(TemplateView):
    """Markers map view."""

    template_name = "map.html"