# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-29 13:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pmain', '0002_auto_20160329_2112'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customerdb',
            name='customer_ID',
        ),
        migrations.AddField(
            model_name='customerdb',
            name='customer_username',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='customerdb',
            name='customer_status',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
