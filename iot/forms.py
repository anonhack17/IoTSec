from django import forms
from .models import Device, DataPoint, SecurityPolicy

class SecurityPolicyForm(forms.ModelForm):
    class Meta:
        model = SecurityPolicy
        fields = ['device', 'role', 'policy']
        labels = {
            'device': 'Устройство',
            'role': 'Выберите роль',
            'policy': 'Политика безопасности',
        }
        widgets = {
            'policy': forms.Textarea(attrs={'rows': 4, 'cols': 40}),
        }

class DeviceForm(forms.ModelForm):
    class Meta:
        model = Device
        fields = ['name', 'device_type', 'description']

class DataPointForm(forms.ModelForm):
    class Meta:
        model = DataPoint
        fields = ['data']