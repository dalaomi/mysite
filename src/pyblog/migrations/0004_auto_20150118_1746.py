# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pyblog', '0003_comment'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
            ],
            options=None,
            bases=None,
            managers=None,
        ),
        migrations.AddField(
            model_name='post',
            name='status',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
    ]
