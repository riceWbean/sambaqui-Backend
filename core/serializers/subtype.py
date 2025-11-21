from rest_framework import serializers
from core.models.subtype import Subtype

class SubtypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subtype
        fields = '__all__'