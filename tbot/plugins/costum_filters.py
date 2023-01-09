from django.conf import settings
from pyrogram import filters

chat = filters.create(lambda _, __, query: query.chat.id == settings.OWNER_GROUP )
user = filters.create(lambda _, __, query: query.from_user.id in settings.ADMINS)