# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2018-08-02 20:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='tags',
            field=models.TextField(blank=True, help_text='Divide Tags by comma', null=True),
        ),
    ]
