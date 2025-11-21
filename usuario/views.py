from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.exceptions import APIException
from django.contrib.auth.models import Group

from .models import Usuario
from .serializers import UserRegisterSerializer, UserSerializer

class UserViewSet(ModelViewSet):
    permission_classes = [AllowAny]
    queryset = Usuario.objects.all()

    def get_serializer_class(self):
        if self.action == "create":
            return UserRegisterSerializer
        else:
            return UserSerializer

    def create(self, request, *args, **kwargs):
        try:
            image = request.FILES.get('image', None)
            data = request.data.copy()
            if image is not None:
                data['image'] = image

            serializer = UserRegisterSerializer(data=data)
            serializer.is_valid(raise_exception=True)
            serializer.save()

            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        except Group.DoesNotExist as e:
            return Response({"error_code": "GROUP_NOT_FOUND", "message": f"The role passed is not a group: {e}"}, status=status.HTTP_400_BAD_REQUEST)
        except APIException as e:
            return Response({"error_code": "CLOUDINARY_ERROR", "message": f"{e}"})