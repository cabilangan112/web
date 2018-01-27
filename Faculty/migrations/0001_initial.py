# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-01-27 13:23
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='detail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Last_name', models.CharField(max_length=200)),
                ('First_name', models.CharField(max_length=200)),
                ('Subject', models.CharField(max_length=200)),
                ('Evaluation_Date', models.DateField(default=datetime.date.today)),
                ('Time', models.TimeField(blank=True, null=True)),
            ],
        ),
    ]
