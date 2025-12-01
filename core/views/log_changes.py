from rest_framework import viewsets
from core.models.log_changes import LogChanges
from core.serializers.log_changes import LogChangesSerializer

class LogChangesViewSet(viewsets.ModelViewSet):
    queryset = LogChanges.objects.all()
    serializer_class = LogChangesSerializer
