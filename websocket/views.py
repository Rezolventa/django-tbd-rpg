import json
import asyncio
from typing import Optional, Union
from channels.generic.websocket import AsyncWebsocketConsumer
from django.shortcuts import render
from django.views.decorators.http import require_GET


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
            # Убираем автоматический запуск TestSender.send_log()
            # Теперь он будет запускаться только по команде из receive()

        except Exception as e:
            await self._send('system', 500, str(e))
            return

    async def receive(self, text_data=None, bytes_data=None):
        if text_data:
            try:
                text = json.loads(text_data)
                print(text)
                # Добавляем обработку команды для запуска TestSender
                if text.get('command') == 'start_test':
                    sender = TestSender(self)
                    await sender.send_log()
            except Exception as e:
                await self._send('system', 500, str(e))
        return super().receive(text_data, bytes_data)

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
