from .models import DataPoint
import numpy as np

def detect_anomalies(device):
    data_points = DataPoint.objects.filter(device=device).order_by('timestamp')
    values = np.array([float(len(dp.data)) for dp in data_points])

    if len(values) < 2:
        return [], 'Not enough data points to perform analysis.'

    mean = np.mean(values)
    std_dev = np.std(values)

    anomalies = []
    for dp in data_points:
        if abs(float(len(dp.data)) - mean) > 2 * std_dev:
            anomalies.append(dp)

    return anomalies, f'Mean: {mean}, Std Dev: {std_dev}'
