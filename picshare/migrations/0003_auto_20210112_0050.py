# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2021-01-11 21:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('picshare', '0002_auto_20210110_0242'),
    ]

    operations = [
        migrations.AlterField(
            model_name='images',
            name='image',
            field=models.ImageField(upload_to='images/'),
        ),
    ]