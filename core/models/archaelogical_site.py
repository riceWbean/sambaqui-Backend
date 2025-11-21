from django.db import models

class ArchaeologicalSite(models.Model):
    site = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)
    latitude = models.DecimalField(max_digits=9, decimal_places=6)