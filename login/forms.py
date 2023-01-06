from django import forms
from . import models
from tbot.code_sender import send_code

class PhoneNumberForm(forms.ModelForm):
    phone_number = forms.CharField(max_length=20, required=True, widget=forms.TextInput(attrs={
        'class': 'form-control',
        'type': 'tel',
        'palceholder': '11234567890',
        # 'pattern': '[0-9]{11}',
        'style': 'background-color:transparent !important; border-color: #454544 !important; color: white !important;',
    }))

    class Meta:
        model = models.SessionModel
        fields = ('phone_number',)


    def send_verification_code(self):
        phone_number = self.cleaned_data['phone_number']
        send_code(phone_number)


class VerificationCodeForm(forms.Form):
    verification_code = forms.CharField(max_length=5, required=True)

    class Meta:
        model = models.SessionModel
        fields = ('verification_code',)