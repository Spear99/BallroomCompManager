# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-12-22 05:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('competition', '0011_auto_20171221_2058'),
    ]

    operations = [
        migrations.AddField(
            model_name='competition',
            name='event_limit',
            field=models.IntegerField(blank=True, null=True, verbose_name='Event Limit'),
        ),
    ]
