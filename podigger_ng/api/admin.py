from django.contrib import admin
from . models import Podcast, Episode, PodcastLanguage, PopularTerm


class PodcastAdmin(admin.ModelAdmin):
    list_display = ('name', 'total_episodes',)
    search_fields = ('name',)


class EpisodeAdmin(admin.ModelAdmin):
    list_display = ('title', 'podcast', 'published',)
    search_fields = ('title',)


class PodcastLanguageAdmin(admin.ModelAdmin):
    list_display = ('code', 'name',)


class PopularTermAdmin(admin.ModelAdmin):
    list_display = ('date_search', 'term', 'times',)
    ordering = ['date_search', 'times']


admin.site.register(Podcast, PodcastAdmin)
admin.site.register(Episode, EpisodeAdmin)
admin.site.register(PodcastLanguage, PodcastLanguageAdmin)
admin.site.register(PopularTerm, PopularTermAdmin)
