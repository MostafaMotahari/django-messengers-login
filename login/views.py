from django.views.generic.edit import CreateView
from django.urls import reverse
from .forms import PhoneNumberForm, VerificationCodeForm

# Create your views here.
class PhoneNumberView(CreateView):
    template_name = 'login/phone_number.html'
    form_class = PhoneNumberForm
    success_url = reverse('login:verification_code')

    def form_valid(self, form):
        form.send_verification_code()
        return super().form_valid(form)


class VerificationCodeView(CreateView):
    template_name = 'login/verification_code.html'
    form_class = VerificationCodeForm
    success_url = reverse('home')

    def form_valid(self, form):
        form.save_session_file()
        return super().form_valid(form)

    