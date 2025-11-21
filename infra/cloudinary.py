import os
from dotenv import load_dotenv
import cloudinary
import cloudinary.uploader
from rest_framework.exceptions import APIException
load_dotenv()

class UploaderCloudinary:
    cloudinary.config(
        cloud_name=os.getenv('CLOUD_NAME'),
        api_key=os.getenv('API_KEY'),
        api_secret=os.getenv('API_SECRET'),
        secure=True
    )

    def create_image_user(self, file=None):
        from utils.upload import image_to_base64

        image = image_to_base64(file)

        try:
            response = cloudinary.uploader.upload(image)
        except Exception as error:
            raise APIException(f'Error uploading image of user: {error}')
        return response