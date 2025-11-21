from rest_framework.viewsets import ModelViewSet

from core.models import Artefact
from core.serializers import ArtefactSerializer, ArtefactImageSerializer
from rest_framework.exceptions import APIException
from rest_framework.response import Response
from rest_framework import status

class ArtefactViewSet(ModelViewSet):
    queryset = Artefact.objects.prefetch_related("images").all()
    serializer_class = ArtefactSerializer

    def create(self, request, *args, **kwargs):
        serializerArtefact = ArtefactSerializer(data=request.data)
        serializerArtefact.is_valid(raise_exception=True)
        artefact = serializerArtefact.save()

        for file in request.FILES:
            object = {"file": file, "artefact": artefact.id}
            try:
                serializerImage = ArtefactImageSerializer(data=object)
                serializerImage.is_valid(raise_exception=True)
                serializerImage.save()
            except APIException as e:
                return Response({"error_code": "CLOUDINARY_ERROR", "message": f"{e}"})
        
        serializerResponse = ArtefactSerializer(self.queryset)

        return Response(data=serializerResponse.data, status=status.HTTP_201_CREATED)