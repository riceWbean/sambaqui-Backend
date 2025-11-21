from rest_framework import serializers
from core.models.conservation_actions import ConservationAction

class ConservationActionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ConservationAction
        fields = ['id', 'description', 'date', 'artefact']
        read_only_fields = ['id']