from django.db import models
from django.utils.translation import gettext_lazy as _


class User(models.Model):
    name = models.CharField(_("Имя"), max_length=50)
    email = models.EmailField(_("Почта"), unique=True)
    birthday_date = models.DateField(_("Год рождения"), auto_now=True)
    genders = models.ForeignKey("users.Genders", on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(_("Время создания"), auto_now=True)


class Genders(models.Model):
    title = models.CharField(_("Пол"), max_length=20)
