# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-11-19 03:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pagina', '0013_auto_20171118_2153'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clase',
            name='fecha',
            field=models.DateTimeField(),
        ),
    ]
