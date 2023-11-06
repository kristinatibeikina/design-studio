from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import FileExtensionValidator
from django.urls import reverse
from django.core.exceptions import ValidationError


class User(AbstractUser):
    name = models.CharField(max_length=254, verbose_name='ФИО', blank=False)
    username = models.CharField(max_length=254, verbose_name='Логин', unique=True, blank=False)
    email = models.CharField(max_length=254, verbose_name='Почта', unique=True, blank=False)
    password = models.CharField(max_length=254, verbose_name='Пароль', blank=False)

    def __str__(self):
        return self.user.username

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
    user = models.ForeignKey('User', on_delete=models.SET_NULL, null=True)
    date = models.DateTimeField(verbose_name='Время создания заявки', auto_now_add=True)

    def validate_image(fieldfile_obj):
        filesize = fieldfile_obj.file.size
        megabyte_limit = 2.0
        if filesize > megabyte_limit * 1024 * 1024:
            raise ValidationError("Размер превышает %sMB" % str(megabyte_limit))

    photo_file = models.ImageField(max_length=254, upload_to='media/', blank=False,
                                   validators=[validate_image, FileExtensionValidator(allowed_extensions=['png', 'jpg', 'jpeg', 'bmp'])])

    REQUEST_STATUS = (
        ('Новая', 'Новая'),
        ('Принято в работу', 'Принято в работу'),
        ('Выполнено', 'Выполнено'),
    )
    status = models.CharField(max_length=254, choices=REQUEST_STATUS, default='Новая', blank=True,verbose_name="Статус")

    def get_absolute_url(self):
        return reverse('application_list', args=[str(self.id)])


    def __str__(self):
        return f'{self.name} ({self.date})'




