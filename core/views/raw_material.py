from rest_framework import viewsets
from core.models import RawMaterial
from core.serializers.raw_material import RawMaterialSerializer

class RawMaterialViewSet(viewsets.ModelViewSet):
    queryset = RawMaterial.objects.all()
    serializer_class = RawMaterialSerializer
    