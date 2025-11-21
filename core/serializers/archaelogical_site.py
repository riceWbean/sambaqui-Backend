from rest_framework import serializers
from core.models.archaelogical_site import ArchaeologicalSite

class ArchaeologicalSiteSerializer(serializers.ModelSerializer):
    class Meta:
        model = ArchaeologicalSite
        fields = '__all__'
        read_only_fields = ('id',)

