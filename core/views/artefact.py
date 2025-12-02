from rest_framework.viewsets import ModelViewSet

from core.models import Artefact, ArtefactImage, Collection, Localization, RawMaterial, SubType, ArchaeologicalSite
from core.serializers import ArtefactCreateUpdateSerializer, ArtefactListSerializer, ArtefactRetrieveSerializer, ArtefactImageSerializer, CollectionSerializer, LocalizationSerializer, RawMaterialSerializer, SubTypeSerializer, ArchaeologicalSiteSerializer
from core.paginators import ArtefactPagination
from rest_framework.exceptions import APIException
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import action
from rest_framework import filters

class ArtefactViewSet(ModelViewSet):
    def get_serializer_class(self):
        if self.action == "list":
            return ArtefactListSerializer
        elif self.action == "retrieve":
            return ArtefactRetrieveSerializer
        else:
            return ArtefactCreateUpdateSerializer

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
    
    @action(detail=False, methods=['GET'])
    def list_categories(self, request):
        serializerCollection = CollectionSerializer(Collection.objects.all(), many=True)
        serializerLocalization = LocalizationSerializer(Localization.objects.all(), many=True)
        serializerRawMaterial = RawMaterialSerializer(RawMaterial.objects.all(), many=True)
        serializerSubType = SubTypeSerializer(SubType.objects.all(), many=True)
        serializerArchaeologicalSite = ArchaeologicalSiteSerializer(ArchaeologicalSite.objects.all(), many=True)

        response = {
            "collections": serializerCollection.data,
            "localizations": serializerLocalization.data,
            "raw_materials": serializerRawMaterial.data,
            "sub_type": serializerSubType.data,
            "archaeological_sites": serializerArchaeologicalSite.data
        }

        return Response(data=response, status=status.HTTP_200_OK)
    
    @action(detail=False, methods=['GET'])
    def list_dashboard(self, request):
        total_artefacts = Artefact.objects.all().count()
        total_collections = Collection.objects.all().count()
        total_archaelogical_site = ArchaeologicalSite.objects.all().count()
        total_raw_materials = RawMaterial.objects.all().count()

        return Response(data={
            "total_artefacts": total_artefacts,
            "total_collections": total_collections,
            "total_archaelogical_site": total_archaelogical_site,
            "total_raw_materials": total_raw_materials
        }, status=status.HTTP_200_OK)

    def create(self, request, *args, **kwargs):
        serializerArtefact = ArtefactCreateUpdateSerializer(data=request.data)
        serializerArtefact.is_valid(raise_exception=True)
        artefact = serializerArtefact.save()

        images = request.FILES.getlist("files")

        print(images)

        for file in images:
            object = {"file": file, "artefact": artefact.id}
            print(object)
            try:
                print(file, object)
                serializerImage = ArtefactImageSerializer(data=object)
                serializerImage.is_valid(raise_exception=True)
                serializerImage.save()
            except APIException as e:
                return Response({"error_code": "CLOUDINARY_ERROR", "message": f"{e}"}, status=status.HTTP_400_BAD_REQUEST)
        
        serializerResponse = ArtefactCreateUpdateSerializer(artefact)

        return Response(data=serializerResponse.data, status=status.HTTP_201_CREATED)
    
    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializerArtefact = ArtefactCreateUpdateSerializer(instance=instance, data=request.data, partial=True)
        serializerArtefact.is_valid(raise_exception=True)
        artefact = serializerArtefact.save()

        images = request.FILES.getlist("files")
        public_ids_cloudinary = request.data.getlist("public_ids_cloudinary", [])

        print(images)

        for index, file in enumerate(images):
            if len(public_ids_cloudinary[index]) <= index: 
                for file in images:
                    object = {"file": file, "artefact": artefact.id}
                    print(object)
                    try:
                        print(file, object)
                        serializerImage = ArtefactImageSerializer(data=object)
                        serializerImage.is_valid(raise_exception=True)
                        serializerImage.save()
                    except APIException as e:
                        return Response({"error_code": "CLOUDINARY_ERROR", "message": f"{e}"}, status=status.HTTP_400_BAD_REQUEST)
            else:
                object = {"file": file, "artefact": artefact.id, "public_id_cloudinary": public_ids_cloudinary[index]}
                print(object)

                instance_image = ArtefactImage.objects.get(public_id_cloudinary=object.get("public_id_cloudinary"))

                try:
                    print(file, object)
                    serializerImage = ArtefactImageSerializer(instance=instance_image, data=object, partial=True)
                    serializerImage.is_valid(raise_exception=True)
                    serializerImage.save()
                except APIException as e:
                    return Response({"error_code": "CLOUDINARY_ERROR", "message": f"{e}"}, status=status.HTTP_400_BAD_REQUEST)
            
        serializerResponse = ArtefactCreateUpdateSerializer(artefact)

        return Response(data=serializerResponse.data, status=status.HTTP_201_CREATED)