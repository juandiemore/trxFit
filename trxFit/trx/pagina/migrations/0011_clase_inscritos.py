# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-11-19 02:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pagina', '0010_salon_sede'),
    ]

    operations = [
        migrations.AddField(
            model_name='clase',
            name='inscritos',
            field=models.IntegerField(default=0),
        ),
    ]
