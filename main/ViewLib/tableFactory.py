from ..models import *
from ..TestLib.Logger import *

class TableFactory:
    def __init__(self):
        self.slug_database = {
            'movies': Movie,
            'videogames': VideoGame,
            'boardgames': BoardGame,
            'mangas' : Manga,
            'animes' : Anime,
        }
        self.slug_csv_fields = {
            'movies' : MovieCsvData,
            'videogames' : VideoGameCsvData,
            'boardgames' : BoardGameCsvData,
            'mangas' : MangaCsvData,
            'animes' : AnimeCsvData,
        }

    def getDBObject(self, db_table):
        if not db_table or not db_table in self.slug_database.keys():
            LOG.error('Invalid table requested for DB Object.')
        return self.slug_database[db_table]

    def getCSVFieldsObj(self, db_table):
        if not db_table or not db_table in self.slug_csv_fields.keys():
            LOG.error('Invalid table requested for CSV headers.')
        return self.slug_csv_fields[db_table]

tables = TableFactory()