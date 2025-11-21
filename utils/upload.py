import base64
from infra.cloudinary import UploaderCloudinary
from PIL import Image

def image_to_base64(file):
    file_content = file.read()

    image = Image.open(file)
    image.verify()
    print(image.format)

    if image.format not in ["JPEG", "JPG", "PNG"]:
        raise TypeError("Invalid image format")
    
    base64_file = base64.b64encode(file_content).decode('utf-8')

    return f"data:image/{image.format.lower()};base64,{base64_file}"

def create_image_user(file):
    uploader = UploaderCloudinary()
    response = uploader.create_image_user(file=file)

    return response

def update_image(file):
    uploader = UploaderCloudinary()
    response = uploader.update_image(file=file)

    return response