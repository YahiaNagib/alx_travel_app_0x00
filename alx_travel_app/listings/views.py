# tasks/views.py
from rest_framework import generics
from .models import Property
from .serializers import PropertySerializer

# ListAPIView automatically handles fetching all items and serializing them
class PropertyList(generics.ListCreateAPIView):
    queryset = Property.objects.all()
    serializer_class = PropertySerializer