
from pyrogram.client import Client
from decouple import config

# Create a new bot
bot = Client(
    "Escorial",
    api_hash=config('API_HASH'),
    api_id=config('API_ID'),
    bot_token=config('BOT_TOKEN'),
    plugins=dict(root='tbot/plugins'),
)