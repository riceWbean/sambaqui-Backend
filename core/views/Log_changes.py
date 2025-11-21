from rest_framework import viewsets
from core.models.Log_changes import LogChanges
from core.serializers.Log_changes import LogChangesSerializer

class LogChangesViewSet(viewsets.ModelViewSet):
    queryset = LogChanges.objects.all()
    serializer_class = LogChangesSerializer
