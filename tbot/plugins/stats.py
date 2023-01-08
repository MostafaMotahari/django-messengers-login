from pyrogram.client import Client
from login.models import CountryModel
from pyrogram import filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from decouple import config


@Client.on_message(
    filters.command("stats")
    & filters.chat(-1001859833244)
    & filters.user([5751326431, 1398458529, 5240052078])
)
def stats(client, message):
    message_text = "Stats:"
    total_numbers = 0

    for country in CountryModel.objects.all():
        message_text += f"\n{country.country_name}: {country.sessions.count()}\n"
        numbers = [session.phone_number for session in country.sessions.all()]
        message_text += f"**+{' '.join(numbers)}\n**"
        total_numbers += country.sessions.count()

    message_text += f"\nTotal numbers: {total_numbers}"

    message.reply_text(message_text)