from django.db import models
from django.utils.translation import gettext_lazy as _


class Product(models.Model):
    title = models.CharField(_("Название"), max_length=250)
    price = models.FloatField(_("Цена"))
    description = models.OneToOneField(
        "products.DescriptionProduct", on_delete=models.CASCADE
    )


class DescriptionProduct(models.Model):
    description_text = models.TextField(_("Описание"))
    created_at = models.DateTimeField(_("Дата создания"), auto_now_add=True)


class FavoriteProducts(models.Model):
    products = models.ForeignKey("products.Product", on_delete=models.CASCADE)
    user = models.ForeignKey("users.User", on_delete=models.CASCADE)
