from rest_framework import serializers
from core.models.sub_type import SubType

class SubTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubType
        fields = '__all__'