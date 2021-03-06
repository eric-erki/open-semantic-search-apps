# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2018-06-28 20:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('setup', '0003_neo4j'),
    ]

    operations = [
        migrations.AddField(
            model_name='setup',
            name='segmentation_pages',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='setup',
            name='graph_neo4j_browser',
            field=models.CharField(blank=True, max_length=1000),
        ),
        migrations.AlterField(
            model_name='setup',
            name='graph_neo4j_host',
            field=models.CharField(blank=True, max_length=1000),
        ),
        migrations.AlterField(
            model_name='setup',
            name='graph_neo4j_password',
            field=models.CharField(blank=True, max_length=1000),
        ),
        migrations.AlterField(
            model_name='setup',
            name='graph_neo4j_user',
            field=models.CharField(blank=True, max_length=1000),
        ),
    ]
