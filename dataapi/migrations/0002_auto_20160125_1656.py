# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dataapi', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cust_db_model',
            old_name='search_id',
            new_name='db_host',
        ),
        migrations.RenameField(
            model_name='cust_db_model',
            old_name='db_collection',
            new_name='db_table',
        ),
    ]
