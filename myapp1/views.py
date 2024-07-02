from django.shortcuts import render
from django.http import HttpResponse
import datetime

# Create your views here.
def current(request):
    dt=datetime.datetime.now()
    resp="<h1>Current Date and Time is %s</h1>"%(dt)
    return HttpResponse(resp)
