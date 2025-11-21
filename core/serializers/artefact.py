from rest_framework.serializers import ModelSerializer

from core.models import Artefact

class ArtefactSerializer(ModelSerializer):
    class Meta:
        model = Artefact
        fields = ['name', 'other_name', 'dimension_length', 'dimension_width', 'weigth', 'dating','conservation_status', 'completeness', 'description', 'observation', 'register_date', 'bibliographic_reference', 'reserved', 'images']