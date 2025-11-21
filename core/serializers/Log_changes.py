from rest_framework import serializers
from core.models.Log_changes import LogChanges

class LogChangesSerializer(serializers.ModelSerializer):
    class Meta:
        model = LogChanges
        fields = ['id', 'change_type', 'changed_by', 'change_date', 'description', 'artefact']
        read_only_fields = ['id']

    def validate_change_date(self, value):
        if value > serializers.datetime.date.today():
            raise serializers.ValidationError("The change date cannot be in the future.")
        return value