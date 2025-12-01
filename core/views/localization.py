from rest_framework import viewsets
from core.models import Localization
from core.serializers.localization import LocalizationSerializer

class LocalizationViewSet(viewsets.ModelViewSet):
    queryset = Localization.objects.all()
    serializer_class = LocalizationSerializer