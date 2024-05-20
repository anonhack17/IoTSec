from django.shortcuts import render, redirect, get_object_or_404
from .forms import DeviceForm, DataPointForm
from .analysis import detect_anomalies
from .models import Device, DataPoint

def add_data_point(request, device_id):
    device = get_object_or_404(Device, pk=device_id)
    if request.method == 'POST':
        form = DataPointForm(request.POST)
        if form.is_valid():
            data_point = form.save(commit=False)
            data_point.device = device
            data_point.save()
            return redirect('device_detail', device_id=device.id)
    else:
        form = DataPointForm()
    return render(request, 'iot/add_data_point.html', {'form': form, 'device': device})
def home(request):
    return render(request, 'iot/home.html')
def analyze_device_data(request, device_id):
    device = get_object_or_404(Device, id=device_id)
    anomalies, stats = detect_anomalies(device)
    return render(request, 'iot/analyze_device_data.html', {
        'device': device,
        'anomalies': anomalies,
        'stats': stats
    })
def device_list(request):
    devices = Device.objects.all()
    return render(request, 'iot/device_list.html', {'devices': devices})

def device_detail(request, device_id):
    device = get_object_or_404(Device, id=device_id)
    data_points = DataPoint.objects.filter(device=device).order_by('-timestamp')[:100]
    anomalies = detect_anomalies(device)
    return render(request, 'iot/device_detail.html', {
        'device': device,
        'data_points': data_points,
        'anomalies': anomalies
    })


def add_device(request):
    if request.method == 'POST':
        form = DeviceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('device_list')
    else:
        form = DeviceForm()

    return render(request, 'iot/add_device.html', {'form': form})
def iot_data(request):
    return render(request, 'iot/iot_data.html')

# iot/views.py

