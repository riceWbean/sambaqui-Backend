from django.db import models
from .artefact import Artefact


class LogMovement(models.Model):
    artefact = models.ForeignKey(Artefact, on_delete=models.PROTECT)
    out_date = models.DateField()
    return_date = models.DateField()