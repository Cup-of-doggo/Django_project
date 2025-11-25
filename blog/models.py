from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length=150, verbose_name='Заголовок')
    content = models.TextField(verbose_name='содержимое')
    preview = models.ImageField(upload_to='blog/', verbose_name='превью', blank=True, null=True)
    created_at = models.DateField(auto_now_add=True, verbose_name='Дата создания')
    updated_at = models.DateField(auto_now=True, verbose_name='Дата последнего изменения')
    publication_sign = models.BooleanField(default=True, verbose_name='признак публикации')
    views_count = models.PositiveIntegerField(default=0, verbose_name='количество просмотров')

    def __str__(self):
        return (f'Название: {self.title}, Дата: {self.created_at}, '
                f'Количество просмотров: {self.views_count}')

    class Meta:
        verbose_name = 'Блог'
        verbose_name_plural = 'Блоги'
        ordering = ['title',]