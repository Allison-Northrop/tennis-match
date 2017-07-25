# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-25 20:59
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('player', '0009_auto_20170725_1318'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player_attributes',
            name='username',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]