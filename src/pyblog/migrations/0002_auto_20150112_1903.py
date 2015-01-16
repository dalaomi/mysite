# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pyblog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='comment_num',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='post',
            name='read_num',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
    ]
