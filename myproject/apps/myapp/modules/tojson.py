import json
from django.core import serializers

def polls(polls):
    data = json.dumps([{
        'id': p.id,
        'title': p.title,
        'description': p.description} for p in polls])
    # data = serializers.serialize('json', polls)
    return data

