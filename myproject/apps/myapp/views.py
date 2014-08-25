from django.shortcuts import render, HttpResponse, get_object_or_404, get_list_or_404
from myproject.apps.myapp.models import Poll
from myproject.apps.myapp.modules import tojson

def index(request):
    return render(request, 'index.html')


def polls(request, extension=None):
    polls = get_list_or_404(Poll.objects.all().order_by('-id'))
    
    if not extension:  # extension json|xml
        return render(request, 'polls.html', {'polls': polls})
    elif extension == 'json':
        return HttpResponse(tojson.polls(polls), content_type='application/json')
