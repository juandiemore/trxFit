# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-11-18 22:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pagina', '0007_entrenador_especialidad'),
    ]

    operations = [
        migrations.AddField(
            model_name='entrenador',
            name='foto',
            field=models.ImageField(blank=True, upload_to=b''),
        ),
    ]
