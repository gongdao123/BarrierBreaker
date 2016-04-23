# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('Proxys', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='httpproxy',
            name='created_datetime',
            field=models.DateTimeField(default=datetime.datetime(2016, 2, 20, 13, 55, 20, 57504, tzinfo=utc), verbose_name=b'created_datetime', auto_now_add=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='httpproxy',
            name='modified_datetime',
            field=models.DateTimeField(default=datetime.datetime(2016, 2, 20, 13, 55, 28, 336713, tzinfo=utc), blank=True),
            preserve_default=False,
        ),
    ]
