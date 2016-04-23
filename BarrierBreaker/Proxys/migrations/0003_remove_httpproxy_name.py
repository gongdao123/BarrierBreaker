# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Proxys', '0002_auto_20160220_1355'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='httpproxy',
            name='name',
        ),
    ]
