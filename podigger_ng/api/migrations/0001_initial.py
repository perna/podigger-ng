# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-22 23:06
from __future__ import unicode_literals

import datetime
import django.contrib.postgres.fields.jsonb
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Episode',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=255)),
                ('link', models.URLField(max_length=255, unique=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('published', models.DateTimeField(blank=True, null=True)),
                ('enclosure', models.URLField(blank=True, max_length=255, null=True)),
                ('to_json', django.contrib.postgres.fields.jsonb.JSONField(blank=True, null=True)),
            ],
            options={
                'db_table': 'episode',
            },
        ),
        migrations.CreateModel(
            name='Podcast',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=128, unique=True)),
                ('feed', models.CharField(max_length=255, unique=True)),
                ('image', models.TextField(blank=True, default='/static/dist/img/podcast-banner.png', null=True)),
                ('total_episodes', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'ordering': ['name'],
                'db_table': 'podcast',
            },
        ),
        migrations.CreateModel(
            name='PodcastLanguage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('code', models.CharField(default='pt', max_length=20, null=True)),
                ('name', models.CharField(default='português', max_length=60, null=True)),
            ],
            options={
                'ordering': ['name'],
                'db_table': 'podcast_language',
            },
        ),
        migrations.CreateModel(
            name='PopularTerm',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('term', models.CharField(max_length=255)),
                ('times', models.IntegerField(default=1)),
                ('date_search', models.DateField(blank=True, default=datetime.datetime(2017, 6, 22, 23, 6, 54, 6057), null=True)),
            ],
            options={
                'ordering': ['date_search'],
                'db_table': 'popular_term',
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=255, unique=True)),
            ],
            options={
                'db_table': 'tag',
            },
        ),
        migrations.CreateModel(
            name='TopicSuggestion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True, null=True)),
                ('is_recorded', models.BooleanField()),
            ],
            options={
                'db_table': 'topic_suggestion',
            },
        ),
        migrations.AddField(
            model_name='podcast',
            name='language',
            field=models.ForeignKey(blank=True, default=1, null=True, on_delete=django.db.models.deletion.CASCADE, to='api.PodcastLanguage'),
        ),
        migrations.AddField(
            model_name='episode',
            name='podcast',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='api.Podcast'),
        ),
        migrations.AddField(
            model_name='episode',
            name='tags',
            field=models.ManyToManyField(db_table='tags', to='api.Tag'),
        ),
    ]
