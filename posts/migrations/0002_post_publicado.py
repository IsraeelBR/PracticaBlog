# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-07-30 17:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='publicado',
            field=models.BooleanField(default=False),
        ),
    ]
