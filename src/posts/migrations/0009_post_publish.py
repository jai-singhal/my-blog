# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-20 14:09
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0008_remove_post_publish'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='publish',
            field=models.DateField(auto_now_add=True, default=datetime.datetime(2017, 1, 20, 14, 9, 51, 602186, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
