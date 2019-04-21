from django.db import models

# Create your models here.
class Vehicle(models.Model):
    VEHICAL_TYPE = (
    ('TRUCK', 'truck'),
    ('BUS', 'bus'),
    ('AIRPLANE', 'airplane'),
    )
    WORKING_CONDITION = (
    ('WORKING', 'working'),
    ('MAINTENANCEUS', 'maintenanceus')
    )
    vehical_type = models.CharField(max_length=100, choices=VEHICAL_TYPE)
    model_name = models.CharField(max_length=100)
    model_number = models.CharField(max_length=100)
    condition = models.CharField(max_length=100, choices=WORKING_CONDITION)
    
    def __str__(self):
        return self.model_name
    
    