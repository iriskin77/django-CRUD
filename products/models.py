from django.db import models
from django.urls import reverse
# Create your models here.


class Product(models.Model):
    name = models.CharField(max_length=255, verbose_name="Название товара")
    description = models.TextField(verbose_name="Описание товара")
    price = models.IntegerField(verbose_name="Цена товара")
    date = models.DateTimeField(auto_now_add=True, verbose_name="Время добавления товара")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('product_detail', kwargs={'pk': self.id})
