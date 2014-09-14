# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('url', models.URLField()),
                ('priority', models.PositiveSmallIntegerField()),
                ('is_working', models.BooleanField(default=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('name', models.CharField(max_length=20)),
                ('description', models.TextField()),
                ('color', models.CharField(max_length=6, null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Station',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('name', models.CharField(max_length=40)),
                ('description', models.TextField()),
                ('created_at', models.DateTimeField(null=True)),
                ('last_modified_at', models.DateTimeField(null=True)),
                ('last_listened_at', models.DateTimeField(null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='StationGenre',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('genre', models.ForeignKey(to='stations.Genre')),
                ('station', models.ForeignKey(to='stations.Station')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='station',
            name='genres',
            field=models.ManyToManyField(through='stations.StationGenre', to='stations.Genre'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='address',
            name='station',
            field=models.ForeignKey(to='stations.Station'),
            preserve_default=True,
        ),
    ]
