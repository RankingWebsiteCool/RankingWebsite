from django.contrib import admin
from django.urls import path
from . import views

app_name = 'main'

urlpatterns = [
    path('', views.homepage, name = 'homepage'),
    path('test-form', views.testForm, name = 'test_form'),
    path('movies', views.slugHome, name = 'movies_homepage'),
    path('movies/view/<int:items_loaded>/', views.viewRankingTable, name = 'movies_view'),
    path('movies/single/<str:entry_id>/', views.individualPage, name = 'movies_individual_page'),
    path('movies/browse/<int:items_loaded>/', views.chronologicalPage, name = 'movies_browse'),
    path('movies/search/<int:items_loaded>/', views.searchPage, name = 'movies_search'),
    path('videogames', views.slugHome, name = 'videogames_homepage'),
    path('videogames/view/<int:items_loaded>/', views.viewRankingTable, name = 'videogames_view'),
    path('videogames/single/<str:entry_id>/', views.individualPage, name = 'videogames_individual_page'),
    path('videogames/browse/<int:items_loaded>/', views.chronologicalPage, name = 'videogames_browse'),
    path('videogames/search/<int:items_loaded>/', views.searchPage, name = 'videogames_search'),
    path('boardgames', views.slugHome, name = 'boardgames_homepage'),
    path('boardgames/view/<int:items_loaded>/', views.viewRankingTable, name = 'boardgames_view'),
    path('boardgames/single/<str:entry_id>/', views.individualPage, name = 'boardgames_individual_page'),
    path('boardgames/browse/<int:items_loaded>/', views.chronologicalPage, name = 'boardgames_browse'),
    path('boardgames/search/<int:items_loaded>/', views.searchPage, name = 'boardgames_search'),
    path('mangas', views.slugHome, name = 'mangas_homepage'),
    path('mangas/view/<int:items_loaded>/', views.viewRankingTable, name = 'mangas_view'),
    path('mangas/single/<str:entry_id>/', views.individualPage, name = 'mangas_individual_page'),
    path('mangas/browse/<int:items_loaded>/', views.chronologicalPage, name = 'mangas_browse'),
    path('mangas/search/<int:items_loaded>/', views.searchPage, name = 'mangas_search'),
    path('animes', views.slugHome, name = 'animes_homepage'),
    path('animes/view/<int:items_loaded>/', views.viewRankingTable, name = 'animes_view'),
    path('animes/single/<str:entry_id>/', views.individualPage, name = 'animes_individual_page'),
    path('animes/browse/<int:items_loaded>/', views.chronologicalPage, name = 'animes_browse'),
    path('animes/search/<int:items_loaded>/', views.searchPage, name = 'animes_search'),
]
