from rest_framework import viewsets
from core.models.origin import Origin
from core.serializers.origin import OriginSerializer

class OriginViewSet(viewsets.ModelViewSet):
    queryset = Origin.objects.all()
    serializer_class = OriginSerializer

