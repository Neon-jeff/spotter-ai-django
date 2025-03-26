from django.db import models

# Create your models here.

class Trip(models.Model):
    current_location = models.JSONField()
    current_cycle_used = models.IntegerField()
    pickup_location = models.JSONField()
    dropoff_location = models.JSONField()

    def __str__(self) -> str:
        return f'{self.dropoff_location['city']} Trip'
