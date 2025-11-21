from rest_framework.viewsets import ModelViewSet

from core.models import ArtefactImage
from core.serializers import ArtefactImageSerializer

class ArtefactImageViewSet(ModelViewSet):
    queryset = ArtefactImage.objects.all()
    serializer_class = ArtefactImageSerializer