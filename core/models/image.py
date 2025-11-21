from django.db import models

class Image(models.Model):
    public_id_cloudinary = models.CharField(max_length=100)
    url_photo = models.CharField(max_length=255)

    def __str__(self):
        return self.url_photo