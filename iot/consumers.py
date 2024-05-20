from channels.generic.websocket import WebsocketConsumer

class IoTConsumer(WebsocketConsumer):
    def connect(self):
        self.accept()

    def disconnect(self, close_code):
        pass

    def receive(self, text_data):
        # Здесь можно обработать полученные данные от клиента, если это необходимо
        pass
