# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-12-24 18:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('competition', '0017_couple_competition'),
    ]

    operations = [
        migrations.AddField(
            model_name='round',
            name='completed',
            field=models.BooleanField(default=False, verbose_name='Completed'),
        ),
    ]
