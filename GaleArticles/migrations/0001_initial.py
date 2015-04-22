# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ArticleContent',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('articlecontentpath', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='ArticleImage',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('artcicleimage', models.CharField(max_length=100)),
                ('imagetype', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='ArticleModel',
            fields=[
                ('articleid', models.AutoField(primary_key=True, serialize=False)),
                ('category', models.CharField(max_length=100)),
                ('rank', models.IntegerField()),
                ('articlename', models.CharField(max_length=100)),
                ('lastupdated', models.DateTimeField(auto_now=True)),
                ('shortdescription', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Author',
            fields=[
                ('authorid', models.AutoField(primary_key=True, serialize=False)),
                ('authorname', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='RelatedArticle',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('articleid', models.ForeignKey(to='GaleArticles.ArticleModel', related_name='RelatedArticle_articleid')),
                ('category', models.ForeignKey(to='GaleArticles.ArticleModel', related_name='relate_category')),
                ('rel_artcile_id', models.ForeignKey(to='GaleArticles.ArticleModel', related_name='RelatedArticle_articleid_1')),
            ],
        ),
        migrations.AddField(
            model_name='articlemodel',
            name='authorid',
            field=models.ForeignKey(to='GaleArticles.Author', related_name='article_authorid'),
        ),
        migrations.AddField(
            model_name='articleimage',
            name='articleid',
            field=models.ForeignKey(to='GaleArticles.ArticleModel', related_name='ArticleImage_articleid'),
        ),
        migrations.AddField(
            model_name='articlecontent',
            name='articleid',
            field=models.ForeignKey(to='GaleArticles.ArticleModel', related_name='ArticleContent_articleid'),
        ),
    ]
