from django.db import models
from .artefact import Artefact
from .reserve import Reserve

class LogMovement(models.Model):
    artefact = models.ForeignKey(Artefact, on_delete=models.PROTECT)
    reserve = models.ForeignKey(Reserve, on_delete=models.PROTECT)
    out_date = models.DateField()
    return_date = models.DateField(null=True, blank=True)