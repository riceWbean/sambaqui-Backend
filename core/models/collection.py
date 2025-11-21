from django.db import models

class Collection(models.Model):
    name = models.CharField(max_length=100)
    quantity_artefacts = models.PositiveIntegerField()

    def __str__(self):
        return self.name