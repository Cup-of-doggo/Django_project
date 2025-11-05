from django.db import models

class Blog(models.Model):

    title = models.CharField(max_length=150, verbose_name='Заголовок')
    content = models.TextField(verbose_name='содержимое')
    preview = models.ImageField(verbose_name='превью')
    created_at = models.DateField(verbose_name='Дата создания')
    updated_at = models.DateField(verbose_name='Дата последнего изменения')
    publication_sign = models.BooleanField(max_length=150, verbose_name='признак публикации')
    views = models.CharField(max_length=150, verbose_name='количество просмотров')


    def __str__(self):
        return (f'Название: {self.title}, Описание: {self.preview}, '
                f'дата: {self.created_at}, количество просмотров: {self.views}')

    class Meta:
        verbose_name = 'Блог'
        verbose_name_plural = 'Блоги'
        ordering = ['title',]
