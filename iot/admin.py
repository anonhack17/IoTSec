from django.contrib import admin

from iot.models import Device, DataPoint

# Register your models here.
admin.site.register(Device)
admin.site.register(DataPoint)