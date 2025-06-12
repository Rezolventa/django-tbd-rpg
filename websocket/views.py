import json
# from asyncio import sleep
import asyncio
from typing import Optional, Union
from urllib.parse import parse_qs

from asgiref.sync import sync_to_async
from channels.db import database_sync_to_async
from channels.generic.websocket import AsyncWebsocketConsumer
from django.conf import settings
from django.contrib.auth import get_user_model
from django.shortcuts import render
from django.views.decorators.http import require_GET
# from jwt import decode as jwt_decode
# from rest_framework_simplejwt.exceptions import InvalidToken, TokenError
# from rest_framework_simplejwt.tokens import UntypedToken

# from apps.notification.constants import COMMON_GROUP
# from apps.notification.models import HeaderNotification
# from apps.websocket.utils import get_group_name_ws


class TestSender:
    def __init__(self, ws):
        self.delay_list = [1, 2, 4, 5, 7]
        self.ws = ws

    async def send_log(self):
        # Создаем список задач для асинхронного выполнения
        tasks = []
        for delay in self.delay_list:
            # Для каждой задержки создаем отдельную корутину
            async def send_delayed_message(d):
                await asyncio.sleep(d)
                await self.ws._send('notifiable', 200, {"message": f"message_with_delay_{d}"})

            tasks.append(send_delayed_message(delay))

        # Запускаем все задачи параллельно
        await asyncio.gather(*tasks)

        # После выполнения всех задач отправляем сообщение "Done"
        await self.ws._send('notifiable', 200, {"message": "Done!"})


@require_GET
def ws_debug(request):  # type: ignore
    return render(request, 'ws-debug.html', {})


class WsEndpoint(AsyncWebsocketConsumer):
    async def connect(self) -> None:
        try:
            await self.accept()

            # Создаем экземпляр TestSender и запускаем отправку сообщений
            sender = TestSender(self)
            # sender.ws = self
            await sender.send_log()

        except Exception as e:
            await self._send('system', 500, str(e))
            return

    async def receive(self, text_data=None, bytes_data=None):
        if text_data:
            try:
                text = json.loads(text_data)
                print(text)
            #     if text.get('content_type') == 'execute' and text.get('content'):
            #         # Исполняем указанную функцию
            #         await self.__class__.__dict__[text['content']['func']](self)
            # except KeyError:
            #     content = {'error': 'Method not found'}
            #     await self._send('system', 400, content)
            except Exception as e:
                await self._send('system', 500, e.args[1])
        return super().receive(text_data, bytes_data)
        # await super().receive(text_data, bytes_data)
        # return self._send(content_type="some_content_type", status_code=200, content={"message": text_data})

    async def _send(
        self,
        content_type: str,
        status_code: int,
        content: Optional[Union[list, dict]] = None,
    ) -> None:
        await self.send(
            text_data=json.dumps(
                {
                    'content_type': content_type,
                    'status_code': status_code,
                    'content': content,
                }
            )
        )
        if status_code == 500:
            await self.close()
