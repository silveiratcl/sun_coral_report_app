"""
URL mappings for the marker app.
"""

from django.urls import(
    path,
    include,
)

from rest_framework.routers import DefaultRouter

from markers import views

router = DefaultRouter()
router.register('markers', views.MarkerViewSet)

app_name = 'markers'

urlpatterns = [
    path('', include(router.urls)),
]
