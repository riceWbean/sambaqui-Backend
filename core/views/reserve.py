from rest_framework import viewsets
from core.models.reserve import Reserve
from core.serializers.reserve import ReserveSerializer

class ReserveViewSet(viewsets.ModelViewSet):
    queryset = Reserve.objects.all()
    serializer_class = ReserveSerializer
    