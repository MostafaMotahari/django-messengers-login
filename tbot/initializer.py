from django.conf import settings
from pyrogram.client import Client
from decouple import config

# Create a new bot
bot = Client(
    "Escorial",
    api_hash=settings.API_HASH,
    api_id=settings.API_ID,
    bot_token=settings.BOT_TOKEN,
    plugins=dict(root='tbot/plugins'),
)