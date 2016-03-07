from rest_framework import viewsets

from .models import Hop, Aroma
from .serializers import HopSerializer, AromaSerializer


class HopViewSet(viewsets.ModelViewSet):
    queryset = Hop.objects.all().order_by('name')
    serializer_class = HopSerializer
