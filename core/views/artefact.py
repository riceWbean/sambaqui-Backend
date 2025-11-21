from rest_framework.viewsets import ModelViewSet

from core.models import Artefact
from core.serializers import ArtefactCreateSerializer, ArtefactListSerializer, ArtefactRetrieveSerializer, ArtefactImageSerializer
from core.paginators import ArtefactPagination
from rest_framework.exceptions import APIException
from rest_framework.response import Response
from rest_framework import status
from rest_framework import filters
from django.core.paginator import Paginator
from django_filters.rest_framework import DjangoFilterBackend

class ArtefactViewSet(ModelViewSet):
    def get_serializer_class(self):
        if self.action == "list":
            return ArtefactListSerializer
        elif self.action == "retrieve":
            return ArtefactRetrieveSerializer
        else:
            return ArtefactCreateSerializer

    filter_backends = [filters.SearchFilter]
    search_fields = ['name', 'other_name', 'description']
    pagination_class = ArtefactPagination

    def get_queryset(self):
        queryset = Artefact.objects.prefetch_related("images").all().order_by("-id")

        allowed_filters = ['conservation_status', 'completeness', 'detail_conservation_status', 'collection_category', 'ethnic_group', 'technique', 'reserved', 'collection', 'raw_material', 'sub_type', 'archaeological_site']

        for key, value in self.request.GET.items():
            if key in allowed_filters and value:
                print(key)
                queryset = queryset.filter(**{key: value}).order_by("-id")
        
        return queryset

    def create(self, request, *args, **kwargs):
        serializerArtefact = ArtefactCreateSerializer(data=request.data)
        serializerArtefact.is_valid(raise_exception=True)
        artefact = serializerArtefact.save()

        images = request.FILES.getlist("files")

        for file in images:
            object = {"file": file, "artefact": artefact.id}
            try:
                print(file, object)
                serializerImage = ArtefactImageSerializer(data=object)
                serializerImage.is_valid(raise_exception=True)
                serializerImage.save()
            except APIException as e:
                return Response({"error_code": "CLOUDINARY_ERROR", "message": f"{e}"}, status=status.HTTP_400_BAD_REQUEST)
        
        serializerResponse = ArtefactCreateSerializer(artefact)

        return Response(data=serializerResponse.data, status=status.HTTP_201_CREATED)