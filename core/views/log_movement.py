from rest_framework import viewsets
from core.models.log_movement import LogMovement
from core.serializers.log_movement import LogMovementSerializer

class LogMovementViewSet(viewsets.ModelViewSet):
    queryset = LogMovement.objects.all()
    serializer_class = LogMovementSerializer