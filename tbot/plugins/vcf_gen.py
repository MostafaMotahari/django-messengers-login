from pyrogram.client import Client
from pyrogram import filters

# Static variables
TEMPLATE = """BEGIN:VCARD
VERSION:2.1
N:;{};;;
FN:{}
TEL;CELL:+{}
END:VCARD\n"""


@Client.on_message(filters.command("vcf"))
def vcf_generator(client, message):
    message.reply_text("Generating vcf file ...")
    client.send_chat_action(message.chat.id, "typing")

    if len(message.command) == 4:
        phone_number = message.command[1]
        count = int(message.command[2])
        file_name = message.command[3]

        vcf_result = ""

        for i in range(count):
            vcf_result += TEMPLATE.format(f"{file_name}-{i}", f"{file_name}-{i}", phone_number+i)

        with open(f"{file_name}.vcf", "w") as f:
            f.write(vcf_result)

        client.send_document(message.chat.id, f"{file_name}.vcf")