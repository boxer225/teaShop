from django.db import models
from django.urls import reverse_lazy
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    fio = models.CharField(max_length=350, verbose_name='ФИО')
    number_of_phone = models.CharField(max_length=15, verbose_name='Номер телефона')

    def __str__(self):
        return self.username


class Comments(models.Model):
    comment = models.TextField(verbose_name='Отзыв')
    mark = models.IntegerField(verbose_name='Оценка')

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'


class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name='Категория')
    slug = models.SlugField(max_length=255, verbose_name='URL', unique=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse_lazy('category', kwargs={'slug': self.slug})


class Tea(models.Model):
    name = models.CharField(max_length=80, verbose_name='Наименование')
    description = models.TextField(verbose_name='Описание')
    slug = models.SlugField(max_length=255, verbose_name='URL', unique=True)
    price = models.IntegerField(verbose_name='Стоимость')
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    image = models.ImageField(upload_to='photos/%Y/%m/%d/', verbose_name='Фото')
    comment = models.ManyToManyField('Comments', blank=True, related_name='comments')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse_lazy('product', kwargs={'slug': self.slug})

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
        index_together = (('id', 'slug'), )
