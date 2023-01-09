from pyrogram.client import Client
from pyrogram import filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from . import costum_filters
from . import costum_filters


@Client.on_message(filters.command("add") & costum_filters.chat & costum_filters.user)
def add_account(client, message):
    if len(message.command) == 3:
        country_code = message.command[1]
        account = message.command[2]

        client.send_message(
            chat_id=message.chat.id,
            text=f"Login url for +{country_code}{account}:\n",
            reply_markup=InlineKeyboardMarkup(
                [[InlineKeyboardButton(
                    text="Login",
                    url=f"http://89.108.88.184:8000/login/{country_code+account}?country_code={country_code}"
                )]]
            )
        )