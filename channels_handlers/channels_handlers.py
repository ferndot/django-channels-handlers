import json
from pydantic import ValidationError


class ConsumerHandlerMixin:
    """
    Mixin to integrate one or more handlers with a django-channels consumer
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

    async def handle_message(self, message):
        for handler in self.handlers:
            await handler.handle_message(message)

    def serialize_message(self, message):
        return message.json()

    def deserialize_message(self, pickled_message):
        return json.loads(pickled_message)

    @classmethod
    async def encode_json(cls, content):
        try:
            return content.json()
        except AttributeError:
            return await super().encode_json(content)


class MessageHandler:
    """
    Executes different actions based on message type
    """

    namespace = "request"
    handled_types = {}
    models = {}

    def __init__(self, consumer):
        self.consumer = consumer

    async def handle_message(self, message):
        """
        Handles the given message

        :param message: The message to handle
        :returns: The results of the handling function or None if the handler does not
            recognize the message type
        """
        # Check for type
        if "type" not in message:
            raise ValueError("Message must have a type")

        # Get handler function name
        try:
            func_name = self.handled_types[message["type"]]

        except KeyError:
            # Silently exit if the handler does not recognize the message type
            return

        # Validate message
        message = await self.validate_message(message)

        # Fire handler actions
        func = getattr(self, func_name)
        return await func(message)

    async def validate_message(self, message):
        try:
            return self.construct_message(message.pop("type"), message)

        except KeyError:
            return message

        except ValidationError as e:
            await self.consumer.send_json(
                content={
                    "type": f"{self.namespace}.invalid_message",
                    "errors": e.errors(),
                },
                close=4002,
            )

    def construct_message(self, message_type, data):
        model_class = self.models.get(message_type)
        return model_class(**data)

    def serialize_message(self, message_type, data):
        return self.construct_message(message_type, data)
