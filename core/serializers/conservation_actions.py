from rest_framework import serializers
from core.models.conservation_actions import ConservationAction

class ConservationActionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ConservationAction
        fields = ['id', 'description', 'date', 'artefact']
        read_only_fields = ['id']

    def validate_date(self, value):
        if value > serializers.datetime.date.today():
            raise serializers.ValidationError("The date of the conservation action cannot be in the future.")
        return value