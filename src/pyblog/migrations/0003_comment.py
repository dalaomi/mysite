# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('pyblog', '0002_auto_20150112_1903'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('nick_name', models.CharField(max_length=30)),
                ('email', models.CharField(max_length=30)),
                ('site_url', models.CharField(max_length=50)),
                ('comment', models.TextField()),
                ('comment_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('post_id', models.ForeignKey(to='pyblog.Post')),
            ],
            options=None,
            bases=None,
            managers=None,
        ),
    ]
