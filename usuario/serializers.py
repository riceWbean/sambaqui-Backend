from django.db import transaction
from rest_framework.serializers import ModelSerializer, CharField, FileField
from django.contrib.auth.models import Group
from .models import Usuario
from utils.upload import create_image_user

class UserRegisterSerializer(ModelSerializer):
    image = FileField(write_only=True, required=False, allow_null=True)
    role = CharField(write_only=True)
    class Meta:
        model = Usuario
        fields = ['email', 'password', 'role', 'image', 'photo']

    def create(self, validated_data):
        with transaction.atomic():
            image = validated_data.pop('image', None)
            role = validated_data.pop('role', None)
            
            user = Usuario.objects.create_user(**validated_data)

            group = Group.objects.get(name=role)
            user.groups.add(group)

            if image is not None:
                image_response = create_image_user(image)
                print(image_response)
                user.photo = image_response['secure_url']
                user.public_id_cloudinary = image_response['public_id']

            user.save()

            return user

class UserSerializer(ModelSerializer):
    class Meta:
        model = Usuario
        fields = "__all__"