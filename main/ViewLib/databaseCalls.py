from .tableFactory import *
from ..models import HomeService, MediaDataBases
from .common import jsParse, showDebugMessage
from .searchStrings import *
from ..TestLib.Logger import *
import numpy as np
import pdb

BATCH_SIZE = 20
MAX_ACCEPTED_TITLE = 100
MAX_ACCEPTED_POST_ADD = 3 # This is added to the total number of entries in the database

def getTotalNumberEntries(Database):
    try:
        return len(Database.objects.all())
    except:
        LOG.warning('There are no entries in the database requested.')
        return 0

def getDownloadFlag(request):
    if request.method != 'POST': return False
    if not 'downloadFlag' in request.POST.keys(): return False
    if request.POST['downloadFlag'] == 'true': return True
    return False

def addServices():
    context = {}
    context['services'] = [h for h in HomeService.objects.all()]
    return context

## TODO add test for this
def getDatabase(*args, **kwargs):
    split_url = args[0].path.split('/')
    if len(split_url) < 2:
        LOG.warn('Database requested for url that is too short.')
    else:
        return split_url[1]

def pageWithHeader(func):
    def wrapFunc(*args, **kwargs):
        kwargs['context'] = addServices()
        kwargs['download_flag'] = getDownloadFlag(args[0])
        db_table_name = getDatabase(*args, **kwargs)
        kwargs['context']['db_table'] = MediaDataBases.objects.get(slug_name = db_table_name)
        return func(*args, **kwargs)
    return wrapFunc

def addContentStatistics(request, context, items_loaded):
    db_objects = tables.getDBObject(context['db_table'].slug_name)
    total_nr_entries = getTotalNumberEntries(db_objects)
    context['items_selected'] = np.min([items_loaded, total_nr_entries]) * [0]
    context['items_loaded'] = items_loaded
    context['batch_size'] = BATCH_SIZE
    context['total_nr_entries'] = total_nr_entries
    if not 'entries' in context.keys():
        showDebugMessage(request, 'Batch stats added with no entries'); return
    context['js_runtimes'] = jsParse([e.runtime for e in context['entries']])

def getListOfEntriesByRanking(request, context, items_loaded):
    db_objects = tables.getDBObject(context['db_table'].slug_name)
    context['entries'] = [e for e in db_objects.objects.all().filter(
        combined_ranking_order__lt = items_loaded + 1)]
    addContentStatistics(request, context, items_loaded)

def getCurrentEntriesOnReload(request, context, items_loaded):
    current_items = items_loaded
    getListOfEntriesByRanking(request, context, current_items)

def parseUserSelectedEntries(request, context):
    db_objects = tables.getDBObject(context['db_table'].slug_name)
    total_nr_entries = getTotalNumberEntries(db_objects)
    nr_items = len(context['items_selected'])
    if nr_items > total_nr_entries + MAX_ACCEPTED_POST_ADD:
        showDebugMessage(request, 'Submission is too long.'); return
    for key, value in request.POST.items():
        if key == 'csrfmiddlewaretoken' or key[0] != 'e' : continue
        if (value != 'on') :
            showDebugMessage(request, 'Input form has unexpected value.')
            return
        arr_ind = key[1:]
        try: arr_ind = int(arr_ind)
        except:
            showDebugMessage(request, 'Form input does not have expected name.')
            return
        if arr_ind < nr_items : context['items_selected'][arr_ind] = 1
    return context['items_selected']

def addSingleEntryById(request, context, entry_id):
    db_objects = tables.getDBObject(context['db_table'].slug_name)
    try:
        context['single_entry'] = db_objects.objects.get(id = entry_id)
    except:
        default_id = context['db_table'].default_id
        context['single_entry'] = db_objects.objects.get(id = default_id)

def addMultipleEntriesById(entry_ids, context):
    db_objects = tables.getDBObject(context['db_table'].slug_name)
    matched_entries = [e for e in db_objects.objects.all().filter(id__in=entry_ids)]
    matched_entries = sorted(matched_entries, key=lambda e: entry_ids.index(str(e.id)))
    if len(matched_entries) != len(entry_ids): return
    context['entries'] = matched_entries

## TODO add test for this
def reorderJsArray(context, field_name, sort_order):
    context[field_name] = context[field_name][1:-1].split(',')
    context[field_name] = [float(e) for e in context[field_name]]
    reorderArrayByIndex(context, field_name, sort_order)
    context[field_name] = jsParse(context[field_name])

def reorderArrayByIndex(context, field_name, sort_order):
    context[field_name] = [context[field_name][i] for i in sort_order]

## TODO add test for this
def orderEntriesByDate(context):
    release_dates = np.array([e.released_order for e in context['entries']], dtype = np.int32)
    sort_order = np.argsort(release_dates)
    reorderArrayByIndex(context, 'entries', sort_order)
    context['first_year'] = context['entries'][0].release_year
    return sort_order

def sortEntriesUpToByDate(context, sort_to_index):
    release_dates = np.array([
        e.released_order for e in context['entries'][:sort_to_index]],
        dtype = np.int32)
    sort_order = np.argsort(release_dates)
    sort_order = np.hstack((
        sort_order,
        np.arange(sort_to_index, len(context['entries']))
    ))
    reorderArrayByIndex(context, 'entries', sort_order)
    return sort_order

def parseSearchString(request, context):
    db_objects = tables.getDBObject(context['db_table'].slug_name)
    total_nr_entries = getTotalNumberEntries(db_objects)
    nr_items = 0
    for key, value in request.POST.items():
        nr_items += 1
        if key == 'search':
            if type(value) != str: return
            if len(value) == 0: return
            if len(value) > MAX_ACCEPTED_TITLE: return
            return representString(value)
        if nr_items > total_nr_entries + MAX_ACCEPTED_POST_ADD:
            showDebugMessage(request, 'Submission is too long.'); return

def addSearchedEntriesToContext(context, search_query, items_loaded):
    db_objects = tables.getDBObject(context['db_table'].slug_name)
    entries = [e for e in db_objects.objects.all()]
    sorted_entries = sorted(entries,
        key=lambda e: queryStringDistance(
        search_query, e.search_string.split('_'))
    )
    context['entries'] = sorted_entries[:items_loaded]
    context['search_query'] = ','.join([str(e.id) for e in context['entries']])

def checkSearchQuery(request, db_table):
    if request.method != 'POST': return
    nr_items = 0
    db_objects = tables.getDBObject(db_table)
    total_nr_entries = getTotalNumberEntries(db_objects)
    for key, value in request.POST.items():
        nr_items += 1
        if key == 'search_query':
            if type(value) != str: return
            searched_movie_ids = value.split(',')
            if len(searched_movie_ids) > total_nr_entries: return
            return searched_movie_ids
        if nr_items > total_nr_entries + MAX_ACCEPTED_POST_ADD:
            showDebugMessage(request, 'Submission is too long.'); return

def checkWhetherQueryWasMade(request, context):
    search_query = parseSearchString(request, context)
    context['query_made'] = search_query and len(search_query) != 0
    if context['query_made']: return search_query
