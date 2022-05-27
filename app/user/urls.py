"""
URL mappings for the user API
"""

from django.urls import path

from user import views


app_name = 'user'

urlpatterns = [
    path('api/create/', views.CreateUserView.as_view(), name='create'),
    path('api/token/', views.CreateTokenView.as_view(), name='token'),
    path('api/me/', views.ManageUserView.as_view(), name='me'),
]
