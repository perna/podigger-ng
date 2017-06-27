from django.db import models
from django.contrib.postgres.fields import JSONField
import datetime

class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Podcast(BaseModel):
    name = models.CharField(unique=True, max_length=128)
    feed = models.CharField(unique=True, max_length=255)
    language = models.ForeignKey('PodcastLanguage', default=1, blank=True, null=True)
    image = models.TextField(blank=True, null=True, default='/static/dist/img/podcast-banner.png')
    total_episodes = models.IntegerField(blank=True, null=True)

    class Meta:
        ordering = ['name']
        db_table = 'podcast'

    def __str__(self):
        return self.name


class PodcastLanguage(BaseModel):
    code = models.CharField(max_length=20, null=True, default='pt')
    name = models.CharField(max_length=60, null=True, default='português')

    class Meta:
        db_table = 'podcast_language'
        ordering = ['name']

    def __str__(self):
        return self.name


class Tag(BaseModel):
    name = models.CharField(unique=True, max_length=255)

    class Meta:
        db_table = 'tag'

    def __str__(self):
        return self.name


class Episode(BaseModel):
    title = models.CharField(max_length=255)
    link = models.URLField(unique=True, max_length=255)
    description = models.TextField(blank=True, null=True)
    published = models.DateTimeField(blank=True, null=True)
    enclosure = models.URLField(max_length=255, blank=True, null=True)
    podcast = models.ForeignKey('Podcast', models.DO_NOTHING, blank=True, null=True)
    to_json = JSONField(blank=True, null=True)
    tags = models.ManyToManyField(Tag, db_table='tags')

    class Meta:
        db_table = 'episode'

    def __str__(self):
        return self.title


class PopularTerm(BaseModel):
    term = models.CharField(max_length=255)
    times = models.IntegerField(default=1)
    date_search = models.DateField(blank=True, null=True, default=datetime.datetime.today())

    class Meta:
        db_table = 'popular_term'
        ordering = ['date_search']

    def __str__(self):
        return self.term


class TopicSuggestion(BaseModel):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    is_recorded = models.BooleanField()

    class Meta:
        db_table = 'topic_suggestion'

    def __str__(self):
        return self.title