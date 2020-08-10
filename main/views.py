from django.shortcuts import render
from django.http import HttpResponse
from .forms import ContactForm
from .ViewLib.databaseCalls import *
from .ViewLib.downloadCSV import *
import pdb

def homepage(request):
    context = {'media_databases': [m for m in MediaDataBases.objects.all()]}
    return render(request = request,  context = context,
        template_name = 'common/main_home.html')

@pageWithHeader
def slugHome(request, context = {}, download_flag = False):
    return render( request = request,
        template_name = context['db_table'].template_folder + 'home.html',
        context = context
    )

def fillInContactForm(request, context):
    form = ContactForm(request.POST)
    if form.is_valid():
        name = form.cleaned_data['name']
        email = form.cleaned_data['email']
        print(name, email)

@pageWithHeader
def testForm(request, context = {}, download_flag = False):
    if request.method == 'POST': fillInContactForm(request, context)
    context['form'] = ContactForm()
    return render(request = request,
        template_name = context['db_table'].template_folder + 'feedback_form.html',
        context = context)

@pageWithHeader
def viewRankingTable(request, items_loaded = 10, context = {}, download_flag = False):
    if download_flag:
        getCurrentEntriesOnReload(request, context, items_loaded)
        items_selected = parseUserSelectedEntries(request, context)
        return getStreamingCsvView(request, context)
    else:
        if request.method == 'POST':
            getListOfEntriesByRanking(request, context, items_loaded + BATCH_SIZE)
            items_selected = parseUserSelectedEntries(request, context)
        else:
            getListOfEntriesByRanking(request, context, items_loaded)
        return render(request = request,
            template_name = context['db_table'].template_folder + 'view_table.html',
            context = context)

@pageWithHeader
def individualPage(request, entry_id, context = {}, download_flag = False):
    addSingleEntryById(request, context, entry_id)
    return render(request = request,
        template_name = context['db_table'].template_folder + 'view_single.html',
        context = context)

@pageWithHeader
def chronologicalPage(request, items_loaded = 10, context = {}, download_flag = False):
    if download_flag:
        getCurrentEntriesOnReload(request, context, items_loaded)
        chrono_order = orderEntriesByDate(context)
        items_selected = parseUserSelectedEntries(request, context)
        return getStreamingCsvView(request, context)
    else:
        if request.method == 'POST':
            getListOfEntriesByRanking(request, context, items_loaded + BATCH_SIZE)
            partial_order = sortEntriesUpToByDate(context, items_loaded)
            reorderJsArray(context, 'js_runtimes', partial_order)
            parseUserSelectedEntries(request, context)
        else:
            getListOfEntriesByRanking(request, context, items_loaded)
        chrono_order = orderEntriesByDate(context)
        if request.method == 'POST':
            reorderArrayByIndex(context, 'items_selected', chrono_order)
        reorderJsArray(context, 'js_runtimes', chrono_order)
        return render(request = request,
            template_name = context['db_table'].template_folder + 'view_chronological.html',
            context = context)

@pageWithHeader
def searchPage(request, items_loaded = 10, context = {}, download_flag = False):
    if download_flag:
        movie_ids = checkSearchQuery(request, context['db_table'].slug_name)
        if not movie_ids: return
        addContentStatistics(request, context, items_loaded + BATCH_SIZE)
        items_selected = parseUserSelectedEntries(request, context)
        context['items_loaded'] = items_loaded
        addMultipleEntriesById(movie_ids, context)
        return getStreamingCsvView(request, context)
    else:
        search_query = checkWhetherQueryWasMade(request, context)
        if search_query: addSearchedEntriesToContext(context, search_query, items_loaded)
        addContentStatistics(request, context, items_loaded)
        return render(request = request,
            template_name = context['db_table'].template_folder + 'view_search.html',
            context = context)
