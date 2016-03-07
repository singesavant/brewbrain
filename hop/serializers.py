from rest_framework import serializers

from .models import Hop, Aroma

class HopSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hop

class AromaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Aroma
