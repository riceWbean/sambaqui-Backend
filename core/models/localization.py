from django.db import models


class Localization(models.Model):
    room = models.CharField(max_length=100)
    shelf = models.CharField(max_length=100)
    bookcase = models.CharField(max_length=100)



    def __str__(self):
        return f"{self.room}, {self.shelf}, {self.bookcase}"