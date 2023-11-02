from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import FileExtensionValidator


class User(AbstractUser):
    name = models.CharField(max_length=254, verbose_name='ФИО', blank=False)
    username = models.CharField(max_length=254, verbose_name='Логин', unique=True, blank=False)
    email = models.CharField(max_length=254, verbose_name='Почта', unique=True, blank=False)
    password = models.CharField(max_length=254, verbose_name='Пароль', blank=False)

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=254, verbose_name='Выбор категории', blank=False)

    def __str__(self):
        return self.name


class Application(models.Model):
    name = models.CharField(max_length=254, verbose_name='Название заявки', blank=False)
    description = models.TextField(max_length=1000, verbose_name='Описание', blank=False)
    category = models.ForeignKey('Category', on_delete=models.SET_NULL, null=True)
    photo_file = models.ImageField(max_length=254, upload_to='images', blank=False, validators=[FileExtensionValidator(allowed_extensions=['png', 'jpg', 'jpeg', 'bmp'])])
    user = models.ForeignKey('User', on_delete=models.SET_NULL, null=True)
    date = models.DateTimeField(verbose_name='Время создания заявки', auto_now_add=True)
    status = models.CharField(max_length=254, default='Новая')

    def __str__(self):
        return f'{self.name} ({self.date})'




