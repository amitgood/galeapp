# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('GaleArticles', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='articlemodel',
            name='articlename',
        ),
        migrations.RemoveField(
            model_name='articlemodel',
            name='rank',
        ),
    ]
