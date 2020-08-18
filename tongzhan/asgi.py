"""
ASGI config for tongzhanbu project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/howto/deployment/asgi/
"""

import os
import json
from django.core.asgi import get_asgi_application

from .service.face import face
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tzb.settings')

http_application = get_asgi_application()


# websocket asgi服务
async def application(scope, receive, send):
    # 如果请求为http 走 asgi服务器
    if scope['type'] == 'http':
        await http_application(scope, receive, send)
    # 如果请求为socket 走websocket服务
    elif scope['type'] == 'websocket':
        await websocket_application(scope, receive, send)
    else:
        raise Exception('unkown scope type' + scope['type'])

# websocket服务


async def websocket_application(scope, receive, send):
    while True:
        # receive接受赋值给event
        event = await receive()
        # 收到建立链接请求
        if event['type'] == 'websocket.connect':
            # 发布消息，建立请求
            await send({'type': 'websocket.accept'})

        # 收到关闭链接请求
        elif event['type'] == 'websocket.disconnect':
            # 跳出循环
            break

        # 正常收到websocket信息
        elif event['type'] == 'websocket.receive':
            print(event["text"])
            j = json.loads(event['text'])
            # 如果 cmd 为 1001 就去视频对比
            print(j["cmd"])
            if j["cmd"] == 1001:
                # {"cmd":1001,"id":1}
                msg = face(j["id"])
                data = {
                    'code': 0,
                    'msg': "success",
                    'data': msg
                }
                j = json.dumps(data)
                await send({
                    'type': 'websocket.send',
                    'text': j
                })
            else:
                await send({
                    'type': 'websocket.send',
                    'text': 'pong'
                })
        else:
            break
    print('[disconnect]')