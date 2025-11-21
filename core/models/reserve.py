from django.db import models
from .artefact import Artefact

class Reserve(models.Model):
    name = models.CharField(max_length=100)
    cpf = models.CharField(max_length=11)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    artefact = models.ForeignKey(Artefact, on_delete=models.PROTECT)

    def __str__(self):
        return f"Reserve: {self.name} - Artefact ID: {self.artefact.id}"