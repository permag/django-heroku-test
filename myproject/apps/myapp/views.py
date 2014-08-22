from django.shortcuts import render, HttpResponse
from myproject.apps.myapp.models import Poll
from myproject.apps.myapp.modules import tojson

def index(request):
    return render(request, 'index.html')


def polls(request, extension=None):
    polls = Poll.objects.all()
    
    if not extension:  # extension json|xml
        return render(request, 'polls.html', {'polls': polls})
    elif extension == 'json':
        return HttpResponse(tojson.polls(polls), mimetype='application/json')
