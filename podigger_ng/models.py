# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models


class AlembicVersion(models.Model):
    version_num = models.CharField(max_length=32)

    class Meta:
        managed = False
        db_table = 'alembic_version'


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class Episode(models.Model):
    title = models.CharField(max_length=-1)
    link = models.CharField(unique=True, max_length=-1)
    description = models.TextField(blank=True, null=True)
    published = models.DateTimeField(blank=True, null=True)
    enclosure = models.CharField(max_length=-1, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    podcast = models.ForeignKey('Podcast', models.DO_NOTHING, blank=True, null=True)
    to_json = models.TextField(blank=True, null=True)  # This field type is a guess.
    search_vector = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'episode'


class Podcast(models.Model):
    name = models.CharField(unique=True, max_length=-1)
    feed = models.CharField(unique=True, max_length=-1)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    language = models.ForeignKey('PodcastLanguage', models.DO_NOTHING, blank=True, null=True)
    image = models.CharField(max_length=-1, blank=True, null=True)
    total_episodes = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'podcast'


class PodcastLanguage(models.Model):
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    name = models.CharField(max_length=60, blank=True, null=True)
    code = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'podcast_language'


class PopularTerm(models.Model):
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    term = models.CharField(max_length=-1)
    times = models.IntegerField(blank=True, null=True)
    date_search = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'popular_term'


class Tag(models.Model):
    name = models.CharField(unique=True, max_length=-1)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tag'


class Tags(models.Model):
    tag = models.ForeignKey(Tag, models.DO_NOTHING, blank=True, null=True)
    episode = models.ForeignKey(Episode, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tags'


class TopicSuggestion(models.Model):
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    title = models.CharField(max_length=-1)
    description = models.TextField(blank=True, null=True)
    is_recorded = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'topic_suggestion'
