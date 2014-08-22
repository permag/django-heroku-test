from django.utils import simplejson
from django.core import serializers

def polls(polls):
    data = simplejson.dumps([{
        'id': p.id,
        'title': p.title,
        'description': p.description} for p in polls])
    # data = serializers.serialize('json', polls)
    return data

