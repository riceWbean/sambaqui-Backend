from rest_framework import serializers
from core.models.Log_changes import LogChanges

class LogChangesSerializer(serializers.ModelSerializer):
    class Meta:
        model = LogChanges
        fields = ['id', 'change_type', 'changed_by', 'change_date', 'description', 'artefact']
        read_only_fields = ['id']
