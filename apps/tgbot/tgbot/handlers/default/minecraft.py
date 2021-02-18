from core.coretypes import ResponseStatus, ErrorPayload, MinecraftResponse
from httpx import Response

from tgbot.handlers.base import CheckerTargetPortHandler, process_args_for_host_port
from tgbot.handlers.metrics import push_status_metric

minecraft_help_message = """
❓ Получает статистику о Minecraft сервере

Использование:
 `/minecraft <hostname> <port>`
 `/minecraft <hostname>:<port>`
 `/minecraft <hostname>` - автоматически выставит порт 25565
"""


invalid_port = """❗Неправильный порт. Напишите /minecraft чтобы увидеть справку к данному способу проверки."""


class MinecraftCheckerHandler(CheckerTargetPortHandler):
    help_message = minecraft_help_message
    api_endpoint = "minecraft"

    def __init__(self):
        super().__init__()

    async def process_args(self, text: str) -> list:
        return process_args_for_host_port(text, 25565)

    async def prepare_message(self, res: Response):
        message, status = await self.message_std_vals(res)
        if status == ResponseStatus.OK:
            payload = MinecraftResponse(**res.json().get("payload"))
            message += f"✅ 👤{payload.online}/{payload.max_players} 📶{payload.latency}ms"
        if status == ResponseStatus.ERROR:
            payload = ErrorPayload(**res.json().get("payload"))
            message += f"❌️ {payload.message}"
        await push_status_metric(status, self.api_endpoint)
        return message
