# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-01-25 14:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('faculty', '0006_auto_20180125_0918'),
    ]

    operations = [
        migrations.AddField(
            model_name='detail',
            name='Evaluation_Date',
            field=models.DateTimeField(default=1, verbose_name='date Evaluate'),
            preserve_default=False,
        ),
    ]