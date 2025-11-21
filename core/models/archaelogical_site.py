from django.db import models

class ArchaeologicalSite(models.Model):
    site = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    country = models.CharField(max_length=50)