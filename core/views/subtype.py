from rest_framework import viewsets
from core.models import Subtype
from core.serializers.subtype import SubtypeSerializer

class SubtypeViewSet(viewsets.ModelViewSet):
    queryset = Subtype.objects.all()
    serializer_class = SubtypeSerializer