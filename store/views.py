from rest_framework import generics

from .models import Hantem
from .serializers import HantemSerializer


class HantemListView(generics.ListCreateAPIView):
    queryset = Hantem.objects.all()
    serializer_class = HantemSerializer


class HantemDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Hantem.objects.all()
    serializer_class = HantemSerializer
    lookup_field = 'slug'
