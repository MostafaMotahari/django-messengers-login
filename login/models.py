from django.db import models

# Create your models here.
class CountryModel(models.Model):
    country_name = models.CharField(max_length=50)
    country_code = models.CharField(max_length=4)
    number_length_without_code = models.IntegerField()
    flag_emoji = models.CharField(max_length=1)

    def __str__(self):
        return self.country_name


class SessionModel(models.Model):
    country = models.ForeignKey(CountryModel, on_delete=models.CASCADE, related_name='sessions')
    phone_number = models.CharField(max_length=20, unique=True)
    last_verification_code = models.CharField(max_length=5)
    verification_time = models.DateTimeField(auto_now_add=True)
    session_string = models.CharField(max_length=800, unique=True, blank=True, null=True)
    post_id = models.BigIntegerField(blank=True, null=True)
    nitroseen_price = models.IntegerField(default=40)

    def __str__(self):
        return self.phone_number