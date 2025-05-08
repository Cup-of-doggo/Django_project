from django.db import models

from django.db import models

class Product(models.Model):

    product_name = models.CharField(max_length=150, verbose_name='Название')
    description = models.CharField(max_length=150, verbose_name='Описание')
    image = models.ImageField(verbose_name='Изображение')
    category = models.CharField(max_length=150, verbose_name='Категория')
    price = models.CharField(max_length=150, verbose_name='Цена')
    created_at = models.DateField(verbose_name='Дата создания')
    updated_at = models.DateField(verbose_name='Дата последнего изменения')

    def __str__(self):
        return (f'Название: {self.product_name}, Описание товара: {self.description}, '
                f'Цена: {self.price}, Категория: {self.category}')

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
        ordering = ['product_name',]


class Category(models.Model):

    category_name = models.CharField(max_length=150, verbose_name='Название категории')
    description = models.CharField(max_length=150, verbose_name='Описание')

    def __str__(self):
        return f'{self.category_name} {self.description}'

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['category_name',]