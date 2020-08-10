import json
from django.contrib import messages
from django.utils.safestring import mark_safe
from django.template import Library

DEBUG_MESSAGES = False
register = Library()

@register.filter(is_safe=True)
def jsParse(obj):
    return mark_safe(json.dumps(obj))

def showDebugMessage(request, message : str):
    if DEBUG_MESSAGES:
        messages.set_level(request, messages.DEBUG)
        messages.debug(request, message)