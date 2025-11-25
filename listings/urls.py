from django.urls import path
from .views import PropertyList

urlpatterns = [
    # This defines the endpoint http://127.0.0.1:8000/api/properties/
    path('api/properties/', PropertyList.as_view(), name='property-list'),
]