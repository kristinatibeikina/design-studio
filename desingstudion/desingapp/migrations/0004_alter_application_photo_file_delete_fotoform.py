# Generated by Django 4.2.6 on 2023-11-05 08:24

import desingapp.models
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('desingapp', '0003_fotoform'),
    ]

    operations = [
        migrations.AlterField(
            model_name='application',
            name='photo_file',
            field=models.ImageField(max_length=254, upload_to='images', validators=[desingapp.models.Application.validate_image, django.core.validators.FileExtensionValidator(allowed_extensions=['png', 'jpg', 'jpeg', 'bmp'])]),
        ),
        migrations.DeleteModel(
            name='FotoForm',
        ),
    ]
