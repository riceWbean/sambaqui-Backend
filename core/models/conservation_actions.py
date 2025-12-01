from django.db import models
from .artefact import Artefact

class ConservationAction(models.Model):
    description = models.TextField()
    date = models.DateField(auto_now_add=True)
    artefact = models.ForeignKey(Artefact, on_delete=models.PROTECT, related_name='conservation_actions')

    def __str__(self):
        return f"Conservation Action on {self.date} for Artefact ID {self.artefact.id}"