from pyrogram import client

def send_code(phone_number):
    with client.Client("my_account", phone_number=phone_number) as app:
        app.send_code(phone_number)