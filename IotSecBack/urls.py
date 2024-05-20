"""
URL configuration for IotSecBack project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.urls import path
from iot.views import iot_data, device_list,device_detail, add_device, analyze_device_data, home, add_data_point

urlpatterns = [
    path('', home, name='home'),
    path('admin/', admin.site.urls),
    path('data/', iot_data, name='iot_data'),
    path('devices/add/', add_device, name='add_device'),
    path('devices/', device_list, name='device_list'),
    path('devices/<int:device_id>/', device_detail, name='device_detail'),
    path('devices/<int:device_id>/analyze/', analyze_device_data, name='analyze_device_data'),
    path('devices/<int:device_id>/add_data_point/', add_data_point, name='add_data_point'),  # Новый маршрут
]
