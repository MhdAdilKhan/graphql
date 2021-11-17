from django.db import models

from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    email = models.EmailField(blank=False,max_length=255,verbose_name="email")
    mobile = models.CharField(max_length=12,verbose_name="mobile")
    USERNAME_FIELD = "username"
    EMAIL_FIELD = "email"  