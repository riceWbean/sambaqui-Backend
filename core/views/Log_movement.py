from rest_framework import viewsets
from core.models.Log_movement import LogMovement
from core.serializers.Log_movement import LogMovementSerializer

class LogMovementViewSet(viewsets.ModelViewSet):
    queryset = LogMovement.objects.all()
    serializer_class = LogMovementSerializer