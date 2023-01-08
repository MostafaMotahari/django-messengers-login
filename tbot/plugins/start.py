from pyrogram.client import Client
from pyrogram import filters
from decouple import config

@Client.on_message(filters.private & filters.command(["start"]))
def start(client, message):
    message.reply_text(
        f"Hello {message.from_user.first_name}!\n\n"
    )