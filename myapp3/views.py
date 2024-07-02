from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def homefunc(request):
    context={'fruits':['Apple', 'Banana', 'Grapes'],
             'students':['Sehban', 'Farooq']}
    return render(request,"table.html",context)