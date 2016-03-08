from rest_framework import viewsets

from .models import Hop, Aroma
from .serializers import HopSerializer, AromaSerializer


class HopViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Hop.objects.all().order_by('name')
    serializer_class = HopSerializer

class AromaViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Aroma.objects.all().order_by('label')
    serializer_class = AromaSerializer
