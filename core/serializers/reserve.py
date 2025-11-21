from rest_framework import serializers
from core.models.reserve import Reserve

class ReserveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reserve
        fields = '__all__'
