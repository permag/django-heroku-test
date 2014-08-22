from django.shortcuts import render, HttpResponse
from myproject.apps.myapp.models import Poll

def index(request):
    return render(request, 'index.html')


def polls(request):
    polls = Poll.objects.all()
    return render(request, 'polls.html', {'polls': polls})