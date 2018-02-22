# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-02-02 04:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('competition', '0027_auto_20180201_2243'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dance',
            name='event',
        ),
        migrations.AddField(
            model_name='dance',
            name='event',
            field=models.ManyToManyField(related_name='dances', to='competition.Event'),
        ),
    ]
