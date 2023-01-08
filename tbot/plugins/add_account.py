from pyrogram.client import Client
from pyrogram import filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from decouple import config


@Client.on_message(
    filters.command("add")
    & filters.chat(-1001859833244)
    & filters.user([5751326431, 1398458529, 5240052078])
)
def add_account(client, message):
    if len(message.command) == 3:
        country_code = message.command[1]
        account = message.command[2]

        client.send_message(
            chat_id=message.chat.id,
            text=f"Login url for {account}:\n",
            reply_markup=InlineKeyboardMarkup(
                [[InlineKeyboardButton(
                    text="Login",
                    url=f"http://127.0.0.1:8000/login/{country_code+account}?country_code={country_code}"
                )]]
            )
        )