# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2018-12-30 20:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('setup', '0005_hunspell'),
    ]

    operations = [
        migrations.AddField(
            model_name='setup',
            name='segmentation_pages_preview',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='setup',
            name='ocr_languages',
            field=models.CharField(blank=True, default='eng', max_length=300),
        ),
    ]
