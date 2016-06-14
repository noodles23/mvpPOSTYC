# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-05-19 07:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pmain', '0006_delete_custdb'),
    ]

    operations = [
        migrations.CreateModel(
            name='custtouchpoint',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cust_email2', models.CharField(max_length=2000)),
                ('touchpoint_type', models.CharField(max_length=300)),
                ('touchpoint_datasource', models.CharField(blank=True, max_length=200, null=True)),
                ('touchpoint_background', models.CharField(blank=True, max_length=200, null=True)),
                ('touchpoint_date', models.CharField(blank=True, max_length=100, null=True)),
                ('touchpoint_month', models.CharField(blank=True, max_length=100, null=True)),
                ('touchpoint_name', models.CharField(blank=True, max_length=200, null=True)),
                ('touchpoint_owner', models.CharField(blank=True, max_length=100, null=True)),
                ('touchpoint_category', models.CharField(blank=True, max_length=200, null=True)),
                ('touchpoint_amount', models.CharField(blank=True, max_length=200, null=True)),
                ('touchpoint_count', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
    ]
