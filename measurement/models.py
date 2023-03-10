from django.db import models

# TODO: опишите модели датчика (Sensor) и измерения (Measurement)
from django.forms import DateField, DateTimeField


class Sensor(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=100)


class Measurement(models.Model):
    sensors = models.ForeignKey(Sensor, on_delete=models.CASCADE, related_name='measurements', null=True)
    temperature = models.DecimalField(max_digits=5, decimal_places=1)
    created_at = models.DateTimeField(auto_now=True)


