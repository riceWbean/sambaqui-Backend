from rest_framework.serializers import ModelSerializer, SerializerMethodField

from core.models import Artefact
from core.serializers import ArtefactImageSerializer

class ArtefactCreateSerializer(ModelSerializer):
    images = ArtefactImageSerializer(many=True, required=False, allow_null=True, read_only=True)
    class Meta:
        model = Artefact
        fields = [
            "id",
            "name",
            "other_name",
            "dimension_length",
            "dimension_width",
            "weigth",
            "dating",
            "conservation_status",
            "completeness",
            "detail_conservation_status",
            "collection_category",
            "ethnic_group",
            "technique",
            "description",
            "observation",
            "register_date",
            "bibliographic_reference",
            "reserved",
            "localization",
            "collection",
            "raw_material",
            "sub_type",
            "archaeological_site",
            "images",
        ]
        read_only_fields = ["register_date"]

class ArtefactListSerializer(ModelSerializer):
    images = ArtefactImageSerializer(many=True, required=False, allow_null=True)
    class Meta:
        model = Artefact
        fields = [
            "id",
            "name",
            "collection",
            "localization",
            "conservation_status",
            "raw_material",
            "sub_type",
            "images",
        ]
        read_only_fields = ["id", "register_date"]
        depth = 1

class ArtefactRetrieveSerializer(ModelSerializer):
    images = ArtefactImageSerializer(many=True, required=False, allow_null=True)
    class Meta:
        model = Artefact
        fields = [
            "id",
            "name",
            "other_name",
            "dimension_length",
            "dimension_width",
            "weigth",
            "dating",
            "conservation_status",
            "completeness",
            "detail_conservation_status",
            "collection_category",
            "ethnic_group",
            "technique",
            "description",
            "observation",
            "register_date",
            "bibliographic_reference",
            "reserved",
            "localization",
            "collection",
            "raw_material",
            "sub_type",
            "archaeological_site",
            "images",
        ]
        read_only_fields = ["id", "register_date"]
        depth = 1