from django.urls import path
from django.views.generic import TemplateView
from . import views

app_name = 'login'

urlpatterns = [
    # Telegram urls
    path('telegram/', TemplateView.as_view(template_name='telegram/login.html'), name='telegram_login'),
    path('telegram/phone-number/', views.TelegramPhoneNumberView.as_view(), name='telegram_phone_number'),
    path('telegram/verification_code/<str:phone_number>', views.TelegramVerificationCodeView.as_view(), name='telegram_verification_code'),
    path('telegram/done/', TemplateView.as_view(template_name='telegram/done.html'), name='telegram_done'),
    # Whatsapp urls
    # path('telegram/', TemplateView.as_view(template_name='telegram/login.html'), name='login'),
    # path('telegram/phone_number/', views.TelegramPhoneNumberView.as_view(), name='phone_number'),
    # path('telegram/verification_code/', views.TelegramVerificationCodeView.as_view(), name='verification_code'),
    # path('telegram/done/', TemplateView.as_view(template_name='telegram/done.html'), name='done'),
]