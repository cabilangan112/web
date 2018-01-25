# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-01-25 15:02
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('faculty', '0007_detail_evaluation_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='detail',
            name='Faculty_dep',
        ),
        migrations.RemoveField(
            model_name='detail',
            name='Sex',
        ),
        migrations.AddField(
            model_name='detail',
            name='Subject',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='detail',
            name='Time',
            field=models.TimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='detail',
            name='Evaluation_Date',
            field=models.DateField(default=datetime.date.today),
        ),
        migrations.DeleteModel(
            name='Department',
        ),
    ]
