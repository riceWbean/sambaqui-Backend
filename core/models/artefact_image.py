from django.db import models

from .artefact import Artefact

class ArtefactImage(models.Model):
    public_id_cloudinary = models.CharField(max_length=100)
    url_photo = models.CharField(max_length=255)
    artefact = models.ForeignKey(Artefact, on_delete=models.CASCADE, related_name="images")

    def __str__(self):
        return self.url_photo