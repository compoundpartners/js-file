# -*- coding: utf-8 -*-
# Generated by Django 1.11.18 on 2019-02-22 08:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('djangocms_file', '0011_auto_20180914_1503'),
    ]

    operations = [
        migrations.AddField(
            model_name='file',
            name='description',
            field=models.TextField(blank=True, default='', verbose_name='Description'),
        ),
        migrations.AddField(
            model_name='file',
            name='terms',
            field=models.TextField(blank=True, default='', verbose_name='Terms'),
        ),
    ]
