from django import forms
from .models import Device, DataPoint

class DeviceForm(forms.ModelForm):
    class Meta:
        model = Device
        fields = ['name', 'device_type', 'description']

class DataPointForm(forms.ModelForm):
    class Meta:
        model = DataPoint
        fields = ['data']