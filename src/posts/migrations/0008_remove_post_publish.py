# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-20 14:09
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0007_post_publish'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='publish',
        ),
    ]
