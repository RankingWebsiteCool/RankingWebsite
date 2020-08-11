import django
from django.test.client import RequestFactory
from django.core.wsgi import get_wsgi_application
from django.test import Client
from ..Logger import *

import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "RankingMockup.settings")

django.setup()
application = get_wsgi_application()
c = Client()
rf = RequestFactory()

from main.views import *
from main.models import *

def addServices_test():
    services = addServices()
    LOG.test(str(services['services'][0]) == 'View Ranking Table',
        'Ranking table is service is not in services header.')

def downloadFlagRecognised_test():
    request = rf.post('/movies/view/1/', {'downloadFlag': 'true'})
    LOG.test(getDownloadFlag(request),
        'Download flag does not return true when posted.')
    request = rf.post('/movies/view/1/')
    LOG.test(not getDownloadFlag(request),
        'Empty request triggers download flag.')
    response = c.post('/movies/view/1/', {'downloadFlag': 'true'})
    LOG.test(response.streaming_content,
        'Streaming content not returned when download flag is active.')

def addContentStatistics_test():
    request = rf.get('/movies/view/1/')
    context = {'db_table': MediaDataBases.objects.get(slug_name = 'movies')}
    addContentStatistics(request, context, 1)
    LOG.test(context['items_selected'] == [0],
        'One object requested with no history has selection filled in.')
    LOG.test(context['batch_size'] == BATCH_SIZE,
        'Batch size has not been added.')
    request = rf.get('/movies/view/10000/')
    addContentStatistics(request, context, 1)
    LOG.test(len(context['items_selected']) < 2000,
        'Movies load request has not been restricted.')

def getCurrentEntriesOnReload_test():
    request = rf.get('/movies/view/1/')
    context = {'db_table': MediaDataBases.objects.get(slug_name = 'movies')}
    addContentStatistics(request, context, 1) # Used to get batch size
    context = {'db_table': MediaDataBases.objects.get(slug_name = 'movies')}
    getCurrentEntriesOnReload(request, context, 1)
    LOG.test(str(type(context['entries'][0])) == "<class 'main.models.Movie'>",
        'Movie object not added to context when entries reloaded.')
    LOG.test(len(context['entries']) == 1,
        'Items returned on reload not equal to expected figure.')

def getListOfEntriesByRanking_test():
    request = rf.get('/movies/view/1/')
    context = {'db_table': MediaDataBases.objects.get(slug_name = 'movies')}
    getListOfEntriesByRanking(request, context, 1)
    LOG.test(str(type(context['entries'][0])) == "<class 'main.models.Movie'>",
        'Movie object not added to context when top movie requested.')
    LOG.test(len(context['entries']) == 1,
        'Items returned on query by ranking not equal to expected figure.')

def parseUserSelectedEntries_test():
    request = rf.post('/movies/view/1/', {'e0': 'on', 'csrfmiddlewaretoken': 'on', 'poop': 0})
    context = {'items_selected': [0], 'db_table': MediaDataBases.objects.get(slug_name = 'movies')}
    items_selected = parseUserSelectedEntries(request, context)
    LOG.test(str(type(items_selected)) == "<class 'list'>",
        'User selected items should be a list after parsing.')
    LOG.test(len(items_selected) == 1,
        'User selected items has changed sized after parsing.')
    LOG.test(items_selected[0] == 1,
        'User selected items has not been parsed.')

def addSingleEntryById_test():
    request = rf.get('/movies/view/1/')
    context = {'db_table': MediaDataBases.objects.get(slug_name = 'movies')}
    addSingleEntryById(request, context, 'i0000169547') # American beaty
    LOG.test(str(type(context['single_entry'])) == "<class 'main.models.Movie'>",
        'Movie object not added to context when movie requested by Id.')

def addMultipleEntriesById_test():
    context = {'db_table': MediaDataBases.objects.get(slug_name = 'movies')}
    entry_ids = ['i0000169547', 'i0000258068', 'i0000243655']
    # American beaty, Quiet American, Wet Hot American Summer (ideally better to mock movies)
    addMultipleEntriesById(entry_ids, context)
    LOG.test(str(type(context['entries'][2])) == "<class 'main.models.Movie'>",
        'Movie object not added when entries requested by Id.')

def orderEntriesByDate_test():
    context = {'db_table': MediaDataBases.objects.get(slug_name = 'movies')}
    entry_ids = ['i0000169547', 'i0000258068', 'i0000243655']
    addMultipleEntriesById(entry_ids, context)
    orderEntriesByDate(context)
    entry_dates = [e.release_year for e in context['entries']]
    LOG.test(entry_dates[0] >= entry_dates[1] and entry_dates[1] >= entry_dates[2],
        'Entries have not been sorted.')

def parseSearchString_test():
    request = rf.post('/movies/view/1/', {'search': 'The Potatoe Farmer',
        'csrfmiddlewaretoken': 'thingey', 'e0': 'off'})
    context = {'db_table': MediaDataBases.objects.get(slug_name = 'movies')}
    parsed_str_list = parseSearchString(request, context)
    LOG.test(parsed_str_list[0] == 'PTT' and parsed_str_list[1] == 'FRMR',
        'Search string not parsed as expected.')

def addSearchedEntriesToContext_test():
    context = {'db_table': MediaDataBases.objects.get(slug_name = 'movies')}
    addSearchedEntriesToContext(context, ['GDFTHR'], 3)
    for movie in context['entries']:
        LOG.test('Godfather' in movie.title,
            'God father cannot be searched.')

def checkSearchQuery_test():
    entry_ids = ['i0000169547', 'i0000258068', 'i0000243655']
    request = rf.post('/movies/view/1/', {
        'search_query': ','.join(entry_ids),
        'csrfmiddlewaretoken': 'thingey', 'e0': 'on'})
    parsed_array = checkSearchQuery(request, 'movies')
    LOG.test(entry_ids == parsed_array,
        'Searched movie array is not returned.')

def checkWhetherQueryWasMade_test():
    context = {'db_table': MediaDataBases.objects.get(slug_name = 'movies')}
    request = rf.get('/movies/view/1/')
    LOG.test(not checkWhetherQueryWasMade(request, context),
        'Request with no query returned nothing.')
    request = rf.post('/movies/view/1/', {'search': ''})
    LOG.test(not checkWhetherQueryWasMade(request, context),
        'Empty query string returned something.')
    request = rf.post('/movies/view/1/', {'search': 'Quazzle'})
    LOG.test(checkWhetherQueryWasMade(request, context),
        'Valid query string returned nothing.')
