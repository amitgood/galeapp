# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('GaleArticles', '0002_auto_20150422_2220'),
    ]

    operations = [
        migrations.AddField(
            model_name='articlemodel',
            name='articlename',
            field=models.CharField(max_length=100, default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='articlemodel',
            name='rank',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
