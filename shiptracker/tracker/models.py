from django.db import models


class Hazard(models.Model):
    latitude = models.FloatField()
    longitude = models.FloatField()
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Hazard at ({self.latitude}, {self.longitude})"
