from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class User(AbstractUser):

    phone_number = PhoneNumberField(
        verbose_name="Номер телефона",
        region=settings.NUMBER_REGION,
        unique=True,
    )
    username = models.CharField(
        verbose_name="Логин",
        max_length=settings.MAX_LEN_USERNAME_USER_MODEL,
        validators=[UnicodeUsernameValidator()],
        null=True,
        blank=True,
        unique=True,
    )
    first_name = models.CharField(
        verbose_name="Имя",
        max_length=settings.MAX_LEN_FIRST_NAME,
        null=True,
        blank=True,
    )
    last_name = models.CharField(
        verbose_name="Фамилия",
        max_length=settings.MAX_LEN_LAST_NAME,
        null=True,
        blank=True,
    )
    email = models.CharField(
        verbose_name="Почта",
        max_length=settings.MAX_LEN_EMAIL_USER_MODEL,
        null=True,
        blank=True,
        unique=True,
    )
    invite_code = models.CharField(
        verbose_name="Инвайт-код",
        max_length=settings.INVITE_CODE_LENGTH,
        blank=True,
        null=True,
        editable=False,
    )
    inviter = models.ForeignKey(
        "self",
        related_name="invitings",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )

    class Meta:
        ordering = ("username",)
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

    def __str__(self) -> str:
        return str(self.phone_number)
