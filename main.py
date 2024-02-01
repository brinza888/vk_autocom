from vk_api.vk_api import VkApi
from vk_api.bot_longpoll import *

GROUP_ID = 176036515
TEXT = "Это автоматический комментарий от сообщества!"

with open("token.txt") as f:
    TOKEN = f.readline().strip()

vk = VkApi(token=TOKEN)
bot = VkBotLongPoll(vk, GROUP_ID)

for event in bot.listen():
    if event.type == VkBotEventType.WALL_POST_NEW:
        vk.method("wall.createComment", {
            "owner_id": event.obj.get("owner_id"),
            "post_id": event.obj.get("id"),
            "message": TEXT,
        })
