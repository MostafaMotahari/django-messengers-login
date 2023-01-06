from django.views.generic.edit import CreateView, UpdateView
from django.urls import reverse_lazy
from .forms import PhoneNumberForm, VerificationCodeForm

# Create your views here.
class TelegramPhoneNumberView(CreateView):
    template_name = 'telegram/phone_num.html'
    form_class = PhoneNumberForm
    success_url = reverse_lazy('login:telegram_verification_code')

    def form_valid(self, form):
        form.send_verification_code()
        return super().form_valid(form)


class TelegramVerificationCodeView(UpdateView):
    template_name = 'telegram/verification.html'
    form_class = VerificationCodeForm
    success_url = reverse_lazy('login:telegram_done')

    def form_valid(self, form):
        form.save_session_file()
        return super().form_valid(form)

    