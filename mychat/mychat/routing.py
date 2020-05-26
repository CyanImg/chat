from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
import wechat.routing

application = ProtocolTypeRouter({
    # 暂时为空，下文填充
    'websocket': AuthMiddlewareStack(
        URLRouter(
            wechat.routing.websocket_urlpatterns
        )
    ),
})

