from rest_framework.viewsets import ModelViewSet

from core.models import Image
from core.serializers import ImageSerializer

class ImageViewSet(ModelViewSet):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer