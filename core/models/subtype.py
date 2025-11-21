from django.db import models
from .rawmaterial import RawMaterial

class Subtype(models.Model):
    name = models.CharField(max_length=50)
    raw_material = models.ForeignKey(RawMaterial, on_delete=models.PROTECT, related_name='subtypes')

    def __str__(self):
        return self.name    
