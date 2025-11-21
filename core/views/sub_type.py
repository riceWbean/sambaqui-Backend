from rest_framework import viewsets
from core.models import SubType
from core.serializers.sub_type import SubTypeSerializer

class SubTypeViewSet(viewsets.ModelViewSet):
    queryset = SubType.objects.all()
    serializer_class = SubTypeSerializer