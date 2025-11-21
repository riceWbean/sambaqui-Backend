from rest_framework.serializers import ModelSerializer, CharField, FileField

from core.models import ArtefactImage
from utils.upload import create_image_user

class ArtefactImageSerializer(ModelSerializer):
    public_id_cloudinary = CharField(required=False, allow_null=True)
    url_photo = CharField(required=False, allow_null=True)
    file = FileField(write_only=True)
    class Meta:
        model = ArtefactImage
        fields = ['public_id_cloudinary', 'url_photo', 'artefact', 'file']

    def create(self, validated_data):
        image_response = create_image_user(validated_data.get('file'))

        object = {"public_id_cloudinary": image_response['public_id'], "url_photo": image_response['secure_url'], "artefact": validated_data.get('artefact')}

        artefact_image = ArtefactImage.objects.create(**object)

        return artefact_image