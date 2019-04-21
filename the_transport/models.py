from django.db import models

class Country(models.Model):
    place = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    zone = models.CharField(max_length=100)

    def __str__(self):
        return self.place