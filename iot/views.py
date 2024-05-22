from django.shortcuts import render, redirect, get_object_or_404
from .forms import DeviceForm, DataPointForm
from .analysis import detect_anomalies
from .models import Device, DataPoint
from django.contrib.auth.decorators import login_required
from .forms import SecurityPolicyForm
from .models import SecurityPolicy

@login_required
def add_security_policy(request, device_id):
    device = get_object_or_404(Device, id=device_id)
    if request.method == 'POST':
        form = SecurityPolicyForm(request.POST)
        if form.is_valid():
            policy = form.save(commit=False)
            policy.device = device
            policy.save()
            return redirect('device_detail', device_id=device.id)
    else:
        form = SecurityPolicyForm()
    return render(request, 'iot/add_security_policy.html', {'form': form, 'device': device})

@login_required
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
@login_required
def analyze_device_data(request, device_id):
    device = get_object_or_404(Device, id=device_id)
    anomalies, stats = detect_anomalies(device)
    return render(request, 'iot/analyze_device_data.html', {
        'device': device,
        'anomalies': anomalies,
        'stats': stats
    })

@login_required
def device_list(request):
    devices = Device.objects.all()
    return render(request, 'iot/device_list.html', {'devices': devices})
@login_required
def device_detail(request, device_id):
    device = get_object_or_404(Device, id=device_id)
    data_points = DataPoint.objects.filter(device=device).order_by('-timestamp')[:100]
    policies = SecurityPolicy.objects.filter(device=device)
    anomalies = detect_anomalies(device)
    return render(request, 'iot/device_detail.html', {
        'device': device,
        'data_points': data_points,
        'anomalies': anomalies,
        'policies': policies
    })

@login_required
def add_device(request):
    if request.method == 'POST':
        form = DeviceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('device_list')
    else:
        form = DeviceForm()

    return render(request, 'iot/add_device.html', {'form': form})

@login_required
def iot_data(request):
    return render(request, 'iot/iot_data.html')

# iot/views.py

@login_required
def edit_device(request, device_id):
    device = get_object_or_404(Device, id=device_id)
    if request.method == 'POST':
        form = DeviceForm(request.POST, instance=device)
        if form.is_valid():
            form.save()
            return redirect('device_detail', device_id=device.id)
    else:
        form = DeviceForm(instance=device)
    return render(request, 'iot/edit_device.html', {'form': form})

@login_required
def delete_device(request, device_id):
    device = get_object_or_404(Device, id=device_id)
    if request.method == 'POST':
        device.delete()
        return redirect('device_list')
    return render(request, 'iot/delete_device.html', {'device': device})


@login_required
def edit_security_policy(request, policy_id):
    policy = get_object_or_404(SecurityPolicy, id=policy_id)
    if request.method == 'POST':
        form = SecurityPolicyForm(request.POST, instance=policy)
        if form.is_valid():
            form.save()
            return redirect('device_detail', device_id=policy.device.id)
    else:
        form = SecurityPolicyForm(instance=policy)
    return render(request, 'iot/edit_security_policy.html', {'form': form, 'policy': policy})

@login_required

def delete_security_policy(request, policy_id):
    policy = get_object_or_404(SecurityPolicy, id=policy_id)
    device_id = policy.device.id
    if request.method == 'POST':
        policy.delete()
        return redirect('device_detail', device_id=device_id)
    return render(request, 'iot/delete_security_policy.html', {'policy': policy})