from django import forms
from . import models

class PhoneNumberForm(forms.Form):
    phone_number = forms.CharField(max_length=20, required=True)

    class Meta:
        model = models.SessionModel
        fields = ('phone_number',)


class VerificationCodeForm(forms.Form):
    verification_code = forms.CharField(max_length=5, required=True)

    class Meta:
        model = models.SessionModel
        fields = ('verification_code',)