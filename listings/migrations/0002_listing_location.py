# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2018-06-03 09:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='listing',
            name='location',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
    ]
