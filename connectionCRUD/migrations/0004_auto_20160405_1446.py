# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-04-05 06:46
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('connectionCRUD', '0003_auto_20160405_1441'),
    ]

    operations = [
        migrations.RenameField(
            model_name='conn',
            old_name='datasource_name',
            new_name='name',
        ),
    ]
