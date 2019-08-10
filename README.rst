django-channels-handlers
========================

.. image:: https://img.shields.io/pypi/v/channels_handlers.svg
    :target: https://pypi.python.org/pypi/channels_handlers
    :alt: Latest PyPI version

.. image:: https://travis-ci.com/joshua-s/django-channels-handlers.svg?branch=master
    :target: https://travis-ci.com/joshua-s/django-channels-handlers

Django Channels, without the Pain 💊


Requirements
------------

- Django>=2.1
- channels>=2.2
- pydantic>=0.32


Usage
-----

Install django-channels-handlers from pypi::

    pip install django-channels-handlers

Create a message handler

.. code:: python

    from channels_handlers.handlers import MessageHandler
    # For async, import AsyncMessageHandler
    

    class ChatHandler(MessageHandler):
        namespace = "chat"
        handled_types = {
            "chat.message": "receive_message",
        }
        models = {
            "chat.message": pydantic_models.Message,
        }

        def receive_message(self, message):
            # Do something with the message
            pass

Import ConsumerHandlerMixin and add it to your Django Channels consumer

.. code:: python

    from channels_handlers.consumers import ConsumerHandlerMixin
    # For async, import AsyncConsumerHandlerMixin
    from channels.generic.websocket import JsonWebsocketConsumer


    class MyConsumer(ConsumerHandlerMixin, JsonWebsocketConsumer):
        handler_classes = [ChatHandler]


Compatibility
-------------

`django-channels-handlers` is compatible with Python 3.6+, Django 2.1+, and Django Channels 2.2+.


License
-------

`django-channels-handlers` is licensed under the MIT License.


Authors
-------

`django-channels-handlers` was written by `Josh Smith <josh@joshsmith.codes>`_.
