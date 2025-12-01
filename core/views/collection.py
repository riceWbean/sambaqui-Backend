from rest_framework.viewsets import ModelViewSet

from core.models import Collection
from core.serializers import CollectionSerializer

class CollectionViewSet(ModelViewSet):
    queryset = Collection.objects.all()
    serializer_class = CollectionSerializer