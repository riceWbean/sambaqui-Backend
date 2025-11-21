from django.db import models

class Changes(models.IntegerChoices):
    CREATE = 1, "Create"
    UPDATE = 2, "Update"
    DELETE = 3, "Delete"


class LogChanges(models.Model):
    user = models.CharField(max_length=100)
    change = models.IntegerField(choices=Changes.choices)
    date_time = models.DateTimeField()
    reason = models.TextField()
    table_name = models.CharField(max_length=50)
    record_id = models.PositiveIntegerField()
    