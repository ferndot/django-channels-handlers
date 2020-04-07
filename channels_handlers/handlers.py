import pydantic


class MessageHandler:
    """
    Executes different actions based on message type
    """

    namespace = "request"
    handled_types = {}
    models = {}

    def __init__(self, consumer):
        self.consumer = consumer

    def _get_handler_function(self, message):
        # Check for type
        if "type" not in message:
            raise ValueError("Message must have a type")

        # Get handler function name
        try:
            # Check if a custom handler is defined
            func_name = self.handled_types[message["type"]]

        except KeyError:
            message_namespace, message_function = message.type.split(".")
            if message_namespace == self.namespace and callable(
                getattr(self, message_function, None)
            ):
                # We can automatically determine the name
                func_name = message_function

            else:
                # Silently exit if the handler does not recognize the message type
                return

        return getattr(self, func_name)

    def _run_message_validation(self, message):
        try:
            return self.construct_message(message.pop("type"), message)

        except KeyError:
            return message

    def construct_message(self, message_type, data):
        model_class = self.models.get(message_type)
        return model_class(**data)

    def handle_message(self, message):
        """
        Handles the given message

        :param message: The message to handle
        :returns: The results of the handling function or None if the handler does not
            recognize the message type
        """

        # Get handler function
        handler_function = self._get_handler_function(message)

        # Validate message
        message = self.validate_message(message)

        # Fire handler actions
        return handler_function(message)

    def receive_json(self, json):
        # Execute any parent logic first
        super().receive_json(json)

        # Handle message
        self.handle_message(json)

    def validate_message(self, message):
        try:
            return self._run_message_validation(message)

        except pydantic.ValidationError as e:
            self.consumer.send_json(
                content={
                    "type": f"{self.namespace}.invalid_message",
                    "errors": e.errors(),
                },
                close=4002,
            )


class AsyncMessageHandler(MessageHandler):
    async def handle_message(self, message):
        """
        Handles the given message

        :param message: The message to handle
        :returns: The results of the handling function or None if the handler does not
            recognize the message type
        """

        # Get handler function
        handler_function = self._get_handler_function(message)

        # Validate message
        message = await self.validate_message(message)

        # Fire handler actions
        return await handler_function(message)

    async def receive_json(self, json):
        # Execute any parent logic first
        await super().receive_json(json)

        # Handle message
        await self.handle_message(json)

    async def validate_message(self, message):
        try:
            return self._run_message_validation(message)

        except pydantic.ValidationError as e:
            await self.consumer.send_json(
                content={
                    "type": f"{self.namespace}.invalid_message",
                    "errors": e.errors(),
                },
                close=4002,
            )
