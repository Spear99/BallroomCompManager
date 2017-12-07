# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-11-30 17:10
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('competitor', '0005_dancer_ownedstudio'),
    ]

    operations = [
        migrations.CreateModel(
            name='StudioRequest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256, verbose_name='Name')),
                ('address', models.CharField(max_length=512, verbose_name='Address')),
                ('city', models.CharField(max_length=256, verbose_name='City')),
                ('state', models.IntegerField(choices=[(0, 'AL'), (1, 'AK'), (2, 'AZ'), (3, 'AR'), (4, 'CA'), (5, 'CO'), (6, 'CT'), (7, 'DE'), (8, 'FL'), (9, 'GA'), (10, 'HI'), (11, 'ID'), (12, 'IL'), (13, 'IN'), (14, 'IA'), (15, 'KS'), (16, 'KY'), (17, 'LA'), (18, 'ME'), (19, 'MD'), (20, 'MA'), (21, 'MI'), (22, 'MN'), (23, 'MS'), (24, 'MO'), (25, 'MT'), (26, 'NE'), (27, 'NV'), (28, 'NH'), (29, 'NJ'), (30, 'NM'), (31, 'NY'), (32, 'NC'), (33, 'ND'), (34, 'OH'), (35, 'OK'), (36, 'OR'), (37, 'PA'), (38, 'RI'), (39, 'SC'), (40, 'SD'), (41, 'TN'), (42, 'TX'), (43, 'UT'), (44, 'VT'), (45, 'VA'), (46, 'WA'), (47, 'WV'), (48, 'WI'), (49, 'WY')], verbose_name='State')),
                ('zip_code', models.IntegerField(verbose_name='Zip Code')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='studio_request', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.RenameField(
            model_name='dancer',
            old_name='ownedStudio',
            new_name='owned_studio',
        ),
    ]
