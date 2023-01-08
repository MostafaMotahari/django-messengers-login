from django import forms
from . import models


class VerificationCodeForm(forms.Form):
    phone_number = forms.CharField(max_length=20, required=True)
    verification_code = forms.CharField(max_length=5, required=True, widget=forms.TextInput(attrs={
        'class': 'form-control',
        'style': 'background-color:transparent !important; border-color: #454544 !important; color: white !important;',
        'type': 'number',
        'placeholder': 'Verification Code',
        'maxlength': '5',
        'minlength': '5',
    }))
    login_hash = forms.CharField(max_length=800, required=True)
    country_code = forms.CharField(max_length=4, required=True)

    class Meta:
        model = models.SessionModel
        fields = ('verification_code', 'phone_number', )