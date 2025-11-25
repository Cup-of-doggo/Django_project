from users.models import CustomUser
from django.db import models

class Category(models.Model):
    category_name = models.CharField(max_length=150, verbose_name='Название категории')
    description = models.CharField(max_length=100, verbose_name='Описание')


    def __str__(self):
        return f'{self.category_name} {self.description}'

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['category_name',]


class Product(models.Model):
    product_name = models.CharField(max_length=150, verbose_name='Название')
    description = models.CharField(max_length=100, verbose_name='Описание')
    image = models.ImageField(upload_to='products/', verbose_name='Изображение', blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Категория')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Цена')
    created_at = models.DateField(auto_now_add=True, verbose_name='Дата создания')
    updated_at = models.DateField(auto_now=True, verbose_name='Дата последнего изменения')
    is_published = models.BooleanField(default=False, verbose_name='статус публикации')
    owner = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='products',null=True,blank=True)


    def __str__(self):
        return (f'Название: {self.product_name}, Описание товара: {self.description}, '
                f'Цена: {self.price}, Категория: {self.category}')


    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
        ordering = ['product_name',]
        permissions = [
            ("can_unpublish_product", "Can unpublish product"),

        ]