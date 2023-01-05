from django.db import models

# Create your models here.
class SessionModel(models.Model):
    phone_number = models.CharField(max_length=20)
    last_verification_code = models.CharField(max_length=5)
    verification_time = models.DateTimeField(auto_now_add=True)
    session_file = models.FileField(upload_to='session_files/')