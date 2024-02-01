from dataclasses import dataclass

from vk_api.vk_api import VkApi
from vk_api.bot_longpoll import *

from config import ConfigClass, load_config


@dataclass
class Config (ConfigClass):
    token: str
    group_id: int
    messages: list[str]

    def __post_init__(self):
        if not self.token:
            raise RuntimeError("No token is provided!")


config = load_config(Config)

vk = VkApi(token=config.token)
bot = VkBotLongPoll(vk, config.group_id)

for event in bot.listen():
    if event.type == VkBotEventType.WALL_POST_NEW:
        for text in config.messages:
            vk.method("wall.createComment", {
                "owner_id": event.obj.get("owner_id"),
                "post_id": event.obj.get("id"),
                "message": text,
            })
