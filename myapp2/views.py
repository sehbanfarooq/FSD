from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime, timedelta
# Create your views here.
def before_after(request,n):
    after=datetime.now()+timedelta(hours=n)
    brfore=datetime.now()-timedelta(hours=n)
    resp="<html><body><h1>%s</h1><br><h2>After 4 hours date and time is %s <br>Before 4 hours date and time is %s<h2></body></html>"%(n,after,brfore)
    return HttpResponse(resp)