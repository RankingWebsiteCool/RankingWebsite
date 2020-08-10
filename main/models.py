from django.db import models
from datetime import datetime

class HomeService(models.Model):
    service_name        = models.CharField(max_length = 30)
    service_description = models.TextField()
    icon_name           = models.CharField(max_length = 30)
    materialize_icon    = models.CharField(max_length = 30)
    short_name          = models.CharField(max_length = 10)
    slug_name           = models.CharField(max_length = 10)

    def __str__(self):
        return self.service_name

class MediaDataBases(models.Model):
    db_description   = models.TextField(null=True)
    materialize_icon = models.CharField(max_length = 30)
    card_name        = models.CharField(max_length = 10)
    source_image     = models.CharField(max_length = 30)
    slug_name        = models.CharField(max_length = 10)
    link_description = models.CharField(max_length = 30)
    template_folder  = models.CharField(max_length = 10)
    page_title       = models.CharField(max_length = 20)
    fa_icon          = models.CharField(max_length = 20)
    image_max_width  = models.PositiveIntegerField()
    default_id       = models.CharField(max_length = 30)

class Movie(models.Model):
    id                     = models.CharField(max_length = 11, primary_key=True)
    title                  = models.CharField(max_length = 100, null=True)
    released_order         = models.PositiveIntegerField(null=True)
    country                = models.CharField(max_length = 30, null=True)
    image                  = models.TextField(null=True)
    certificate            = models.CharField(max_length = 10, null=True)
    plot                   = models.TextField(null=True)
    director               = models.CharField(max_length = 30, null=True)
    language               = models.CharField(max_length = 10, null=True)
    combined_ranking_order = models.PositiveIntegerField(null=True)
    combined_ranking       = models.FloatField(null=True)
    runtime                = models.PositiveIntegerField(null=True)
    release_year           = models.PositiveIntegerField(null=True)
    release_month          = models.CharField(max_length = 9, null=True)
    actors                 = models.CharField(max_length = 250, null=True)
    genre                  = models.CharField(max_length = 30, null=True)
    search_string          = models.CharField(max_length = 100, null=True)

    def __str__(self):
        return self.title

class VideoGame(models.Model):
    id                     = models.PositiveIntegerField(primary_key=True)
    combined_ranking       = models.FloatField(null=True)
    title                  = models.CharField(max_length = 100, null=True)
    summary                = models.TextField(null=True)
    image                  = models.TextField(null=True)
    trailer_url            = models.TextField(null=True)
    combined_ranking_order = models.PositiveIntegerField(null=True)
    released_order         = models.PositiveIntegerField(null=True)
    release_year           = models.PositiveIntegerField(null=True)
    release_month          = models.CharField(max_length = 9, null=True)
    release_day            = models.PositiveIntegerField(null=True)
    runtime                = models.FloatField(null=True)
    players                = models.CharField(max_length = 30, null=True)
    rating                 = models.CharField(max_length = 4, null=True)
    genres                 = models.CharField(max_length = 150, null=True)
    publishers             = models.CharField(max_length = 100, null=True)
    developers             = models.CharField(max_length = 100, null=True)
    search_string          = models.CharField(max_length = 100, null=True)

    def __str__(self):
        return self.title

class BoardGame(models.Model):
    id                     = models.PositiveIntegerField(primary_key=True)
    thumbnail              = models.TextField(null=True)
    image                  = models.TextField(null=True)
    title                  = models.CharField(max_length = 100, null=True)
    summary                = models.TextField(null=True)
    release_year           = models.IntegerField(null=True)
    min_players            = models.PositiveIntegerField(null=True)
    max_players            = models.PositiveIntegerField(null=True)
    best_players           = models.PositiveIntegerField(null=True)
    min_age                = models.PositiveIntegerField(null=True)
    language_dependence    = models.CharField(max_length = 100, null=True)
    difficulty             = models.FloatField(null=True)
    combined_ranking       = models.FloatField(null=True)
    combined_ranking_order = models.PositiveIntegerField(null=True)
    released_order         = models.PositiveIntegerField(null=True)
    search_string          = models.CharField(max_length = 100, null=True)
    runtime                = models.FloatField(null=True)

    def __str__(self):
        return self.title

class Manga(models.Model):
    id                     = models.PositiveIntegerField(primary_key=True)
    title                  = models.CharField(max_length = 120, null=True)
    status                 = models.CharField(max_length = 10, null=True)
    image_url              = models.TextField(null=True)
    type                   = models.CharField(max_length = 10, null=True)
    volumes                = models.PositiveIntegerField(null=True)
    summary                = models.TextField(null=True)
    background             = models.TextField(null=True)
    authors                = models.CharField(max_length = 30, null=True)
    serializations         = models.CharField(max_length = 40, null=True)
    combined_ranking       = models.FloatField(null=True)
    runtime                = models.FloatField(null=True)
    combined_ranking_order = models.PositiveIntegerField(null=True)
    released_order         = models.PositiveIntegerField(null=True)
    release_day            = models.PositiveIntegerField(null=True)
    release_month          = models.CharField(max_length = 3, null=True)
    release_year           = models.PositiveIntegerField(null=True)
    publish_last_day       = models.PositiveIntegerField(null=True)
    publish_last_month     = models.CharField(max_length = 3, null=True)
    publish_last_year      = models.PositiveIntegerField(null=True)
    genres_short           = models.CharField(max_length = 60, null=True)
    genres_long            = models.CharField(max_length = 120, null=True)
    search_string          = models.CharField(max_length = 100, null=True)

    def __str__(self):
        return self.title

class Anime(models.Model):
    id                     = models.PositiveIntegerField(primary_key=True)
    thumbnail              = models.TextField(null=True)
    url_trailer            = models.TextField(null=True)
    title                  = models.CharField(max_length = 120, null=True)
    type                   = models.CharField(max_length = 10, null=True)
    source                 = models.CharField(max_length = 20, null=True)
    episode_count          = models.PositiveIntegerField(null=True)
    status                 = models.CharField(max_length = 20, null=True)
    rating                 = models.CharField(max_length = 30, null=True)
    combined_ranking       = models.FloatField(null=True)
    summary                = models.TextField(null=True)
    background             = models.TextField(null=True)
    runtime                = models.PositiveIntegerField(null=True)
    combined_ranking_order = models.PositiveIntegerField(null=True)
    search_string          = models.CharField(max_length = 60, null=True)
    released_order         = models.PositiveIntegerField(null=True)
    release_day            = models.PositiveIntegerField(null=True)
    release_month          = models.CharField(max_length = 3, null=True)
    release_year           = models.PositiveIntegerField(null=True)
    aired_to_day           = models.CharField(max_length = 2, null=True)
    aired_to_month         = models.CharField(max_length = 3, null=True)
    aired_to_year          = models.CharField(max_length = 4, null=True)
    genres_short           = models.CharField(max_length = 70, null=True)
    genres_long            = models.CharField(max_length = 100, null=True)
    licensors              = models.CharField(max_length = 40, null=True)
    producers              = models.CharField(max_length = 40, null=True)
    studios                = models.CharField(max_length = 40, null=True)

    def __str__(self):
        return self.title

class MovieCsvData(models.Model):
    header_title = models.CharField(max_length = 20, primary_key=True)
    key_in_table = models.CharField(max_length = 30, null=True)

class VideoGameCsvData(models.Model):
    header_title = models.CharField(max_length = 20, primary_key=True)
    key_in_table = models.CharField(max_length = 30, null=True)

class BoardGameCsvData(models.Model):
    header_title = models.CharField(max_length = 20, primary_key=True)
    key_in_table = models.CharField(max_length = 30, null=True)

class MangaCsvData(models.Model):
    header_title = models.CharField(max_length = 20, primary_key=True)
    key_in_table = models.CharField(max_length = 30, null=True)

class AnimeCsvData(models.Model):
    header_title = models.CharField(max_length = 20, primary_key=True)
    key_in_table = models.CharField(max_length = 30, null=True)
