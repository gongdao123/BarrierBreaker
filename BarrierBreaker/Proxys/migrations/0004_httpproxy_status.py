# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Proxys', '0003_remove_httpproxy_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='httpproxy',
            name='status',
            field=models.BooleanField(default=False),
        ),
    ]
