from django.conf import settings
from pyrogram.client import Client
from pyrogram import filters

# Static variables
TEMPLATE = """BEGIN:VCARD
VERSION:2.1
N:;{};;;
FN:{}
TEL;CELL:+{}
END:VCARD\n"""


@Client.on_message(filters.command("vcf") & filters.user(settings.OWNER_ID))
def vcf_generator(client, message):
    waiting_msg = message.reply_text("Generating vcf file ...")

    if len(message.command) == 4:
        phone_number = int(message.command[1])
        count = int(message.command[2])
        file_name = message.command[3]

        vcf_result = ""

        for i in range(count):
            vcf_result += TEMPLATE.format(f"{file_name}-{i}", f"{file_name}-{i}", phone_number+i)

        with open(f"{file_name}.vcf", "w") as f:
            f.write(vcf_result)

        waiting_msg.edit("Sending vcf file ...")
        client.send_document(message.chat.id, f"{file_name}.vcf")
        waiting_msg.delete()