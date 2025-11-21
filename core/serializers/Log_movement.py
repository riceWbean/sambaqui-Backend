from rest_framework import serializers
from core.models.Log_movement import LogMovement

class LogMovementSerializer(serializers.ModelSerializer):
    class Meta:
        model = LogMovement
        fields = ['id', 'artefact', 'reserve', 'out_date', 'return_date']
        read_only_fields = ['id']

    def validate_out_date(self, value):
        if value > serializers.datetime.date.today():
            raise serializers.ValidationError("The out date cannot be in the future.")
        return value