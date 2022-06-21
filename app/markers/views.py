"""Markers API views."""
from rest_framework import (
    viewsets,
    mixins,
    status,
)
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework_gis import filters
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from django.contrib.gis.geos import Point
from django.views.generic.base import TemplateView


from core.models import Marker
from markers.serializers import MarkerSerializer


class MarkerViewSet(viewsets.ModelViewSet):
    """Marker view set."""

    bbox_filter_field = 'location'
    filter_backends = (filters.InBBoxFilter,)
    queryset = Marker.objects.all()
    serializer_class = MarkerSerializer
    #authentication_classes = [TokenAuthentication]
    # just for visualize if the user is authenticated
    #permission_classes = [IsAuthenticated]

   # def get_queryset(self):
    #    """Retrieve markers for authenticated user"""
     #   return self.queryset.filter(user=self.request.user).order_by('-id')

    #def get_serializer_class(self):
     #   """Return the serializer class for request"""
      #  if self.action == 'list':
       #     return serializers.MarkerSerializer
        #elif self.action == 'upload_image':
         #   return serializers.MarkerImageSerializer #########

        #return self.serializer_class

    #def perform_create(self, serializer):
     #   """Create a new marker"""
      #  serializer.save(user=self.request.user)

    #@action(methods=['POST'], detail=True, url_path='upload_image')
    #def upload_image(self, request, pk=None):
     #   marker = self.get_object()
      #  serializer = self.get_serializer(marker, data=request.data)

       # if serializer.is_valid():
        #    serializer.save()
         #   return Reponse(serializer.data, status=status.HTTP_200_OK)

        #return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class MarkersMapView(TemplateView):
    """Markers map view."""

    template_name = 'map.html'