from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser):
    class Role(models.TextChoices):
        CLIENT = "client", "Client"
        SERVICE_PROVIDER = "service_provider", "Service Provider"
        COURIER = "courier", "Courier"
        ADMIN = "admin", "Admin"  # optional: you can still use is_staff/superuser

    role = models.CharField(max_length=32, choices=Role.choices, default=Role.CLIENT)