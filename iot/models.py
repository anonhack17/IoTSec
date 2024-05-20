# iot/models.py

from django.db import models

class Device(models.Model):
    name = models.CharField(max_length=100)
    device_type = models.CharField(max_length=100)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class DataPoint(models.Model):
    device = models.ForeignKey(Device, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    data = models.TextField()  # Assuming the data from devices is in JSON format

    def __str__(self):
        return f"{self.device.name} - {self.timestamp}"
