from django.contrib import admin
from tinymce.widgets import TinyMCE
from .models import HomeService, Movie, MovieCsvData
from django.db import models

class HomeServiceAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Title', {'fields': ['service_name', 'short_name']}),
        ('Content', {'fields': ['icon_name', 'service_description']}),
    ]

    formfield_overrides = {
        models.TextField: {'widget': TinyMCE()}
    }

class MovieAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Title', {'fields': ['title', 'id']}),
        ('Release', {'fields' : ['released_order', 'release_year', 'release_month']}),
        ('Content', {'fields': ['director', 'plot', 'language', 'country',
            'certificate', 'image', 'actors', 'genre']}),
        ('Statistics', {'fields': ['runtime', 'combined_ranking_order', 'combined_ranking']}),
    ]

    formfield_overrides = {
        models.TextField: {'widget': TinyMCE()}
    }

class MovieCsvDataAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Include CSV Fields', {'fields': ['header_title', 'key_in_movie']})
    ]

# Register your models here.
admin.site.register(HomeService, HomeServiceAdmin)
admin.site.register(Movie, MovieAdmin)
admin.site.register(MovieCsvData, MovieCsvDataAdmin)
