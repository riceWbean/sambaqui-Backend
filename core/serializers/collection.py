from rest_framework.serializers import ModelSerializer

from core.models import Collection

class CollectionSerializer(ModelSerializer):
    class Meta:
        model = Collection
        fields = "__all__"