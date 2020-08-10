import django
from django.test import Client
from django.core.wsgi import get_wsgi_application
from ..Logger import *

import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "RankingMockup.settings")

django.setup()
application = get_wsgi_application()
c = Client()

def movieHomePage_test():
    response = c.get('/movies')
    LOG.test(response.status_code == 200,
        'Movie Homepage did not respond')

def videogameHomePage_test():
    response = c.get('/videogames')
    LOG.test(response.status_code == 200,
        'Videogame Homepage did not respond')

def boardgameHomePage_test():
    response = c.get('/boardgames')
    LOG.test(response.status_code == 200,
        'Boardgame Homepage did not respond')

def mangaHomePage_test():
    response = c.get('/mangas')
    LOG.test(response.status_code == 200,
        'Boardgame Homepage did not respond')

def mangaHomePage_test():
    response = c.get('/animes')
    LOG.test(response.status_code == 200,
        'Boardgame Homepage did not respond')

def movieViewTable_test():
    response = c.get('/movies/view/1/')
    LOG.test(response.status_code == 200,
        'Movie View 1 did not respond')

def viewMovie_test():
    response = c.get('/movies/single/no-id/')
    LOG.test(response.status_code == 200,
        'Movie individual page did not respond')

def movieBrowsePage_test():
    response = c.get('/movies/browse/1/')
    LOG.test(response.status_code == 200,
        'Browse choronological movies page did not respond')

def movieSearchPage_test():
    response = c.get('/movies/search/1/')
    LOG.test(response.status_code == 200,
        'Search movie page did not respond')

def viewAnime_test():
    response = c.get('/animes/single/no-id/')
    LOG.test(response.status_code == 200,
        'Anime individual page did not respond')

def viewVideoGame_test():
    response = c.get('/videogames/single/no-id/')
    LOG.test(response.status_code == 200,
        'Videogame individual page did not respond')

def viewBoardGame_test():
    response = c.get('/boardgames/single/no-id/')
    LOG.test(response.status_code == 200,
        'Boardgame individual page did not respond')

def viewMangas_test():
    response = c.get('/mangas/single/no-id/')
    LOG.test(response.status_code == 200,
        'Manga individual page did not respond')
