# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ArticleModel',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('articleid', models.CharField(max_length=100)),
                ('category', models.CharField(max_length=100)),
                ('relatedid', models.CharField(max_length=300)),
                ('articlename', models.CharField(max_length=100)),
                ('author', models.CharField(max_length=100)),
                ('lastupdated', models.DateTimeField(auto_now=True)),
                ('mainImage', models.CharField(max_length=100)),
                ('contentImage1', models.CharField(max_length=100)),
                ('contentImage2', models.CharField(max_length=100)),
                ('contentImage3', models.CharField(max_length=100)),
                ('shortdescription', models.CharField(max_length=200)),
                ('content', models.CharField(max_length=6000)),
            ],
        ),
    ]
