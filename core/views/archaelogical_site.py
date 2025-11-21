from rest_framework import viewsets
from core.models.archaelogical_site import ArchaeologicalSite
from core.serializers.archaelogical_site import ArchaeologicalSiteSerializer

class ArchaeologicalSiteViewSet(viewsets.ModelViewSet):
    queryset = ArchaeologicalSite.objects.all()
    serializer_class = ArchaeologicalSiteSerializer

