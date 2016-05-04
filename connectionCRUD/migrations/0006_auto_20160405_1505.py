# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-04-05 07:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('connectionCRUD', '0005_auto_20160405_1454'),
    ]

    operations = [
        migrations.AddField(
            model_name='conn',
            name='password_if_required',
            field=models.CharField(blank=True, default='Password', max_length=600, null=True),
        ),
        migrations.AddField(
            model_name='conn',
            name='username_or_apikey',
            field=models.CharField(default='User', max_length=600),
        ),
        migrations.AlterField(
            model_name='conn',
            name='connection_type',
            field=models.CharField(choices=[('API Key', 'API Key'), ('Username Password', 'Username Password')], default='API', max_length=200),
        ),
        migrations.AlterField(
            model_name='conn',
            name='name',
            field=models.CharField(choices=[('Google Analytics', 'Google Analytics'), ('mazda', 'Mazda'), ('nissan', 'Nissan'), ('toyota', 'Toyota'), ('Other', 'Other')], default='Google Analytics', max_length=200),
        ),
    ]
