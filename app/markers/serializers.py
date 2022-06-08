"""Markers serializers."""

from rest_framework_gis import serializers

from core.models import Marker


class MarkerSerializer(serializers.GeoFeatureModelSerializer):
    """Marker GeoJSON serializer."""

    class Meta:
        """Marker serializer meta class."""

        fields = ('id', 'name' )
        geo_field = 'location'
        model = Marker

class MarkerImageSerializer(serializers.ModelSerializer):
    """Serializer for uploading images to marker"""

    class Meta:
        model = Marker
        fields = ['id', 'image']
        read_only_fields = ['id']
        extra_kwargs = {'image':{'required': 'True'}}