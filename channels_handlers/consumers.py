import json


class ConsumerHandlerMixin:
    """
    Integrates one or more handlers with a Django Channels JsonWebsocketConsumer
    """

    handler_classes = []
    models = []

    def __init__(self, *args, **kwargs):
        self._initialize_handlers()
        super().__init__(*args, **kwargs)

    def _initialize_handlers(self):
        """
        Instantiates any provided handlers with the proper context
        """
        self.handlers = [handler(self) for handler in self.handler_classes]

    def handle_message(self, message):
        for handler in self.handlers:
            handler.handle_message(message)

    def serialize_message(self, message):
        return message.json()

    def deserialize_message(self, pickled_message):
        return json.loads(pickled_message)

    @classmethod
    def encode_json(cls, content):
        try:
            return content.json()
        except AttributeError:
            return super().encode_json(content)


class AsyncConsumerHandlerMixin(ConsumerHandlerMixin):
    """
    Asynchronous version of ConsumerHandlerMixin for usage with
    AsyncJsonWebsocketConsumer
    """

    async def handle_message(self, message):
        for handler in self.handlers:
            await handler.handle_message(message)

    @classmethod
    async def encode_json(cls, content):
        try:
            return content.json()
        except AttributeError:
            return await super().encode_json(content)
