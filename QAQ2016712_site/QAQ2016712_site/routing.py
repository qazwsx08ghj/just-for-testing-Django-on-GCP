from channels.routing import ProtocolTypeRouter , URLRouter
from channels.auth import AuthMiddlewareStack
import chatroom_stuff.routing

application = ProtocolTypeRouter({
    # (http->django views is added by default)

    'websocket' : AuthMiddlewareStack(
        URLRouter(
            chatroom_stuff.routing.websocket_urlpatterns
        )
    )
})