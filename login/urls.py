from django.urls import path
from django.views.generic import TemplateView
from . import views

app_name = 'login'

urlpatterns = [
    path('', TemplateView.as_view(template_name='login.html'), name='login'),
    path('phone_number/', views.PhoneNumberView.as_view(), name='phone_number'),
    path('verification_code/', views.VerificationCodeView.as_view(), name='verification_code'),
    path('done/', TemplateView.as_view(template_name='done.html'), name='done'),
]