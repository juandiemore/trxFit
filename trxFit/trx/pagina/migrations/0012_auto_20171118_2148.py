# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-11-19 02:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pagina', '0011_clase_inscritos'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='clase',
            name='inscritos',
        ),
        migrations.AddField(
            model_name='clase',
            name='Capacidad',
            field=models.IntegerField(default=30),
        ),
        migrations.AlterField(
            model_name='clase',
            name='fecha',
            field=models.DateField(auto_now_add=True),
        ),
    ]
