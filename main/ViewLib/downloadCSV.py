from .tableFactory import *
from .common import showDebugMessage
from .searchStrings import stripAccents
from ..models import MovieCsvData, VideoGameCsvData
from django.http import StreamingHttpResponse
import csv
import pdb

class Echo:
    def write(self, value):
        return value

def getHeaderNames(CsvObject):
    return [e.header_title for e in CsvObject.objects.all()]

def getFieldNames(CsvObject):
    return [e.key_in_table for e in CsvObject.objects.all()]

def getSelectedIndices(items_selected, items_loaded):
    item_indices = items_selected.copy()
    item_count = 0
    for idx in range(items_loaded):
        if item_indices[idx] == 1:
            item_count += 1
            item_indices[idx] = item_count
    return item_count, item_indices

def processField(entries, idx, field_value, item_indices):
    if "{}" in field_value:
        processed_field = field_value.format(item_indices[idx])
    else:
        processed_field = entries[idx].__dict__[field_value]
    if type(processed_field) == 'str':
        processed_field = stripAccents(processed_field)
    return processed_field

def getFieldsFromSelectedEntries(entries, items_loaded, items_selected, item_indices, CsvTable):
    rows = [getHeaderNames(CsvTable)]
    fields = getFieldNames(CsvTable)
    rows += ([
        processField(entries, idx, field, item_indices) for field in fields
    ] for idx in range(items_loaded) if items_selected[idx] == 1)
    return rows

def getStreamingCsvView(request, context):
    items_selected = context['items_selected']
    entries = context['entries']
    items_loaded = context['items_loaded']
    CsvTable = tables.getCSVFieldsObj(context['db_table'].slug_name)
    item_count, item_indices = getSelectedIndices(items_selected, items_loaded)
    rows = getFieldsFromSelectedEntries(entries, items_loaded, items_selected, item_indices, CsvTable)
    pseudo_buffer = Echo()
    writer = csv.writer(pseudo_buffer)
    response = StreamingHttpResponse((writer.writerow(row) for row in rows),
                                     content_type="text/csv")
    response['Content-Disposition'] = 'attachment; filename="downloadedList.csv"'
    return response