from django.db import models

class Artefact(models.Model):
    class ConservationStatus(models.IntegerChoices):
        PERFECT = 1, "Perfeito",
        GOOD = 2, "Bom",
        REGULAR = 3, "Regular"
        BAD = 4, "Ruim"
        CRITICAL = 5, "Critical"
        IRRETRIEVABLE = 6, "Irreversível"
    class Completeness(models.IntegerChoices):
        WHOLE = 1, "Inteiro"
        FRAGMENTED = 2, "Fratura"
    class DetailConservationStatus(models.IntegerChoices):
        FRIABLE = 1, "Friável"
        FRACTURE = 2, "Fraturado"
    class CollectionCategory(models.IntegerChoices):
        ARCHAEOLOGICAL = 1, "Archaeological"
    name = models.CharField(max_length=100)
    other_name = models.CharField(max_length=100)
    dimension_length = models.PositiveSmallIntegerField()
    dimension_width = models.PositiveSmallIntegerField()
    weigth = models.PositiveIntegerField()
    dating = models.PositiveSmallIntegerField(null=True, blank=True)
    conservation_status = models.IntegerField(choices=ConservationStatus.choices)
    completeness = models.IntegerField()
    description = models.TextField()
    observation = models.TextField()