from django.db import models

class Flight(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    model = models.CharField(max_length=100, null=True, blank=True)
    latitude = models.FloatField()
    longitude = models.FloatField()

