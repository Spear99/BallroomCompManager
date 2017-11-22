# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-11-22 23:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('competition', '0002_event_max_per_heat'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='max_per_heat',
            field=models.IntegerField(default=0, verbose_name='Max Couples per Heat'),
        ),
    ]
