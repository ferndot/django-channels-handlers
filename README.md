# django-channels-handlers

[![Latest PyPI
version](https://img.shields.io/pypi/v/django-channels-handlers.svg)](https://pypi.python.org/pypi/django-channels-handlers)
[![image](https://travis-ci.com/joshua-s/django-channels-handlers.svg?branch=master)](https://travis-ci.com/joshua-s/django-channels-handlers)

Django Channels consumers, without the Pain 💊

django-channels-handers is an abstraction
for Django Channels that makes it easy to implement elegant protocols
without having to worry about the communication layer.

## Requirements

- Django>=2.1
- channels~=2.4
- pydantic~=1.4

## Usage

Install django-channels-handlers from
pypi:
```bash
pip install django-channels-handlers
```

Create pydantic models for each message you intend to handle. This
allows the handler to validate the message and parse it into an object.

```python
from pydantic import BaseModel, UUID4
from typing import Dict, Optional
from datetime import datetime


class ChatMessage(BaseModel):
    type: str = "chat.message"
    id: UUID4
    thread: UUID4
    sender: UUID4
    content: str
    data: Optional[Dict] = {}
    created: datetime
```

Create a message handler.

This will first validate and parse a message that matches
handled_types using the corresponding
entry in models. It will then execute the
method specified in handled_types,
passing the newly parsed message object.

```python
from channels_handlers.handlers import MessageHandler
# For async, import AsyncMessageHandler


class ChatHandler(MessageHandler):
    namespace = "chat"
    models = {
        "chat.message": ChatMessage,
    }

    def message(self, message):
        # Some logic with message, e.g. save to database
        pass
```

Import ConsumerHandlerMixin and add it to
your Django Channels consumer. Then, add your custom handler to the
consumer's handler_classes.

```python
from channels_handlers.consumers import ConsumerHandlerMixin
# For async, import AsyncConsumerHandlerMixin
from channels.generic.websocket import JsonWebsocketConsumer


class MyConsumer(ConsumerHandlerMixin, JsonWebsocketConsumer):
    handler_classes = [ChatHandler]
```

## Compatibility

django-channels-handlers is compatible
with Python 3.6+, Django 2.1+, and Django Channels 2.2+.

## License

django-channels-handlers is licensed
under the MIT License.

## Authors

See [AUTHORS.md](AUTHORS.md).

## Contributing

django-channels-handlers relies on the contributions of talented coders like you.
See [CONTRIBUTING.md](CONTRIBUTING.md) for more information.
