from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    surname = models.CharField(max_length=254, verbose_name='Фамилия', blank=False)
    name = models.CharField(max_length=254, verbose_name='Имя', blank=False)
    patronymic = models.CharField(max_length=254, verbose_name='Отчество', blank=False)
    username = models.CharField(max_length=254, verbose_name='Логин', unique=True, blank=False)
    email = models.CharField(max_length=254, verbose_name='Почта', unique=True, blank=False)
    password = models.CharField(max_length=254, verbose_name='Пароль', blank=False)

    USERNAME_FIELD = 'username'

    def full_name(self):
        return ' '.join([self.surname, self.name, self.patronymic])

    def __str__(self):
        return self.full_name()
