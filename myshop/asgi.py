import os

from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
import channels_redis


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myshop.settings')

application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    "websocket": AuthMiddlewareStack(
        URLRouter(
            # Django Channels URL routing here
        )
    ),
})

# Channels Redis configuration
application = channels_redis.RedisMiddlewareStack(application)

