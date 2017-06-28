from django.db import models
from django.contrib.postgres.fields import JSONField
import datetime

class BaseModel(models.Model):
    created_at = models.DateTimeField("Criado em", auto_now_add=True)
    updated_at = models.DateTimeField("Atualizado em", auto_now=True)

    class Meta:
        abstract = True


class Podcast(BaseModel):
    name = models.CharField("Nome", unique=True, max_length=128)
    feed = models.CharField("Feed", unique=True, max_length=255)
    language = models.ForeignKey('PodcastLanguage', default=1, blank=True, null=True, verbose_name="Idioma")
    image = models.TextField("Banner", blank=True, null=True, default='/static/dist/img/podcast-banner.png')
    total_episodes = models.IntegerField("Total de Episódios", blank=True, null=True, default=0)

    class Meta:
        ordering = ['name']
        db_table = 'podcast'
        verbose_name = 'Podcast'
        verbose_name_plural = 'Podcasts'
        indexes = [
            models.Index(fields=['name'], name='ix_podcast_name'),
            models.Index(fields=['feed'], name='ix_podcast_feed'),
        ]

    def __str__(self):
        return self.name


class PodcastLanguage(BaseModel):
    code = models.CharField("Código", max_length=20, null=True, default='pt')
    name = models.CharField("Nome", max_length=60, null=True, default='português')

    class Meta:
        db_table = 'podcast_language'
        verbose_name = 'Idioma do podcast'
        verbose_name_plural = 'Idiomas dos podcasts'
        ordering = ['name']

    def __str__(self):
        return self.name


class Tag(BaseModel):
    name = models.CharField("Nome", unique=True, max_length=255)

    class Meta:
        db_table = 'tag'
        verbose_name = 'Tag'
        verbose_name_plural = 'Tags'
        indexes = [
            models.Index(fields=['name'], name='ix_tag_name'),
        ]

    def __str__(self):
        return self.name


class Episode(BaseModel):
    title = models.CharField("Título", max_length=255)
    link = models.URLField("Link", unique=True, max_length=255)
    description = models.TextField("Descrição", blank=True, null=True)
    published = models.DateTimeField("Data da publicaçâo", blank=True, null=True)
    enclosure = models.URLField("URL do podcast", max_length=255, blank=True, null=True)
    podcast = models.ForeignKey('Podcast', on_delete=models.DO_NOTHING, blank=True, null=True, verbose_name='Podcast')
    to_json = JSONField("JSON", blank=True, null=True)
    tags = models.ManyToManyField(Tag, db_table='tags', verbose_name="Tags")

    class Meta:
        db_table = 'episode'
        verbose_name = 'Episódio'
        verbose_name_plural = 'Episódios'
        indexes = [
            models.Index(fields=['link'], name='ix_episode_link'),
        ]

    def __str__(self):
        return self.title


class PopularTerm(BaseModel):
    term = models.CharField("Termo", max_length=255)
    times = models.IntegerField("Numero de vezes", default=1)
    date_search = models.DateField("Data da busca", blank=True, null=True, default=datetime.datetime.today())

    class Meta:
        db_table = 'popular_term'
        verbose_name = 'Termo popular'
        verbose_name_plural = 'Termos populares'
        ordering = ['date_search']
        indexes = [
            models.Index(fields=['term'], name='ix_popular_term_term'),
        ]

    def __str__(self):
        return self.term


class TopicSuggestion(BaseModel):
    title = models.CharField("Título", max_length=255)
    description = models.TextField("Descrição", blank=True, null=True)
    is_recorded = models.BooleanField("Já foi gravado?")

    class Meta:
        db_table = 'topic_suggestion'
        verbose_name = 'Sugestão de Tema'
        verbose_name_plural = 'Sugestões de Temas'
        indexes = [
            models.Index(fields=['title'], name='ix_topic_suggestion_title'),
        ]

    def __str__(self):
        return self.title