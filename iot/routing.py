from django.urls import path
from channels.routing import ProtocolTypeRouter, URLRouter
from iot import consumers

websocket_urlpatterns = [
    path('ws/iot_data/', consumers.IoTConsumer.as_asgi()),
]

application = ProtocolTypeRouter({
    'websocket': URLRouter(
        websocket_urlpatterns
    ),
})