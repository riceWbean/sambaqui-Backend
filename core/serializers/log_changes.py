from rest_framework import serializers
from core.models.log_changes import LogChanges

class LogChangesSerializer(serializers.ModelSerializer):
    class Meta:
        model = LogChanges
        fields = "__all__"
        read_only_fields = ['id']
