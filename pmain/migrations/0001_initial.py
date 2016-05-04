# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-29 09:11
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomerDataSources',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer_id', models.CharField(max_length=600)),
                ('customer_email', models.CharField(max_length=600)),
                ('customer_username', models.CharField(max_length=600)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='CustomerDB',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer_name', models.CharField(max_length=600)),
                ('company_website', models.CharField(max_length=600)),
                ('company_name', models.CharField(max_length=600)),
                ('company_country', models.CharField(max_length=600)),
                ('company_primary_currency', models.CharField(max_length=600)),
                ('customer_status', models.CharField(max_length=100)),
                ('form_status', models.CharField(max_length=100)),
                ('customer_email', models.EmailField(max_length=254)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('customer_username', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='DataSources',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_source_name', models.CharField(max_length=600)),
                ('data_source_type', models.CharField(max_length=600)),
                ('data_source_status', models.CharField(max_length=200)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.AddField(
            model_name='customerdatasources',
            name='data_source_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pmain.DataSources'),
        ),
    ]
