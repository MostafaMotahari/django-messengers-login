from django.contrib import admin
from .models import SessionModel, CountryModel

# Register your models here.
admin.site.register(SessionModel)
admin.site.register(CountryModel)
