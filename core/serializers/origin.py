from rest_framework import serializers
from core.models.origin import Origin

class OriginSerializer(serializers.ModelSerializer):
    class Meta:
        model = Origin
        fields = '__all__'