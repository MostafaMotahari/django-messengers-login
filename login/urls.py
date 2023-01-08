from django.urls import path
from django.views.generic import TemplateView
from . import views

app_name = 'login'

urlpatterns = [
    path('<str:phone_number>', views.verification_code_view, name='verification_code'),
    path('done/', TemplateView.as_view(template_name='done.html'), name='done'),
]