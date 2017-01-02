from django.db import models

class Car(models.Model):
    make = models.CharField(max_length=100)
    series = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    engine_size = models.DecimalField(max_digits=4, decimal_places=2, null=True)
    num_doors = models.IntegerField(null=True)
    top_speed = models.IntegerField(null=True)
    acceleration = models.DecimalField(max_digits=6, decimal_places=2, null=True)
    mpg = models.DecimalField(max_digits=6, decimal_places=2, null=True)
    co2_emissions = models.DecimalField(max_digits=6, decimal_places=2, null=True)
    insurance_group = models.IntegerField(null=True)
    price = models.DecimalField(max_digits=8, decimal_places=2, null=True)
