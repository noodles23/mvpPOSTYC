# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='cust_db_model',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('user_current', models.CharField(max_length=600)),
                ('search_value', models.CharField(max_length=2000, null=True, blank=True)),
                ('search_id', models.CharField(max_length=600, null=True, blank=True)),
                ('db_name', models.CharField(max_length=600)),
                ('db_collection', models.CharField(max_length=600)),
                ('db_username', models.CharField(max_length=600)),
                ('db_password', models.CharField(max_length=600)),
            ],
        ),
    ]
