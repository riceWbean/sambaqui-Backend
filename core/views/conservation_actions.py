from rest_framework import viewsets
from core.models.conservation_actions import ConservationAction
from core.serializers.conservation_actions import ConservationActionSerializer

class ConservationActionViewSet(viewsets.ModelViewSet):
    queryset = ConservationAction.objects.all()
    serializer_class = ConservationActionSerializer

    