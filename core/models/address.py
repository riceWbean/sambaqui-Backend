from django.db import models


class Address(models.Model):
    street = models.CharField(max_length=100)
    number = models.CharField(max_length=5)
    district = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    zip_code = models.CharField(max_length=10)
    nickname = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return f"{self.street}, {self.city}, {self.zip_code}, {self.nickname or 'No Nickname'}"