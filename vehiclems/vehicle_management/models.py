from django.db import models

# vehicle management's model
class Vehicle(models.Model):
    VEHICLE_TYPES = (
        ('Two', 'Two wheelers'),
        ('Three', 'Three wheelers'),
        ('Four', 'Four wheelers'),
    )
    vehicle_number=models.CharField(max_length=25,unique=True, blank=False, null=False)
    vehicle_type=models.CharField(max_length=50,choices=VEHICLE_TYPES)
    vehicle_model=models.CharField(max_length=100)
    vehicle_description=models.TextField()

    def __str__(self):
        return self.vehicle_number



