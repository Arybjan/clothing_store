from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.utils.translation import gettext_lazy as _
from .managers import UserManager


class User(AbstractBaseUser):
    name = models.CharField(_("Имя"), max_length=50)
    email = models.EmailField(_("Почта"), unique=True)

    objects = UserManager

    USERNAME_FIELD = "email"

    class Meta:
        verbose_name = _("Пользователь")
        verbose_name_plural = _("Пользователи")
