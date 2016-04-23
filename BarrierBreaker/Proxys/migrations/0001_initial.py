# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='HttpProxy',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100, null=True, blank=True)),
                ('nick_name', models.CharField(max_length=100, null=True, blank=True)),
                ('hash_id', models.CharField(max_length=100, null=True, blank=True)),
                ('lan_ip', models.CharField(max_length=100, null=True, blank=True)),
            ],
        ),
    ]
