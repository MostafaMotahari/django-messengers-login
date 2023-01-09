from pyrogram.client import Client
from login.models import CountryModel
from pyrogram import filters
from . import costum_filters
from .emojies import emojies


@Client.on_message(filters.command("stats") & costum_filters.chat & costum_filters.user)
def stats(client, message):
    message_text = "💰Stats:"
    total_numbers = 0

    for country in CountryModel.objects.all():
        message_text += f"\n{emojies[country.country_name]} {country.country_name}: {country.sessions.count()}\n"
        numbers = [session.phone_number for session in country.sessions.all()]
        message_text += f"**+{' '.join(numbers)}\n**"
        total_numbers += country.sessions.count()

    message_text += f"\n📱Total numbers: {total_numbers}"

    message.reply_text(message_text)