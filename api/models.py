from django.db import models
from django.core.validators import RegexValidator
from django.contrib.auth.models import AbstractUser
from .managers import UserManager
from random import choice
from string import ascii_letters
from datetime import datetime, timedelta


def token():
    t = ""
    for i in range(6):
        t += choice(ascii_letters)
    return t


class User(AbstractUser):
    phone_number_validator = RegexValidator(
        regex=r"^998([378]{2}|(9[013-57-9]))\d{7}$",
        message="Iltimos telefon raqamini to'g'ri kiriting."
    )
    username = models.CharField(max_length=20, unique=True, null=False, blank=False, verbose_name="Telefon raqam (998991234567)", validators=[phone_number_validator])
    token = models.CharField(max_length=20, null=True, blank=True, verbose_name="Parol")
    first_name  = models.CharField(max_length=100, null=False, blank=False, verbose_name="Ism")
    last_name   = models.CharField(max_length=100, null=False, blank=False, verbose_name="Familiya")
    middle_name = models.CharField(max_length=100, null=False, blank=False, verbose_name="Sharif")
    is_free = models.BooleanField(default=False, verbose_name="To'lov qilgan")
    end_date = models.DateTimeField(null=True, blank=True)
    devices = models.IntegerField(default=0, null=True, blank=True)

    objects = UserManager()

    USERNAME_FIELD = "username"

    def __str__(self):
        return self.username
    
    def save(self, *args, **kwargs):
        self.token = token()
        if self.is_free:
            now = datetime.now()
            end_date = now + timedelta(days=30)
            self.end_date = end_date
        return super().save(*args, **kwargs)

    class Meta:
        verbose_name = "Mijoz"
        verbose_name_plural = "Mijozlar"