from django.db import models

class AnimalObservation(models.Model):
    species = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    timestamp = models.DateTimeField(auto_now_add=True)
    confidence = models.FloatField()

    def __str__(self):
        return f"{self.species} observed at {self.location}"