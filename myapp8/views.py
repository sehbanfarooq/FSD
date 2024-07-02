from django.shortcuts import render

# Create your views here.
from myapp8.forms import project
from django.http  import HttpResponse,HttpResponseRedirect
from myapp8.models import project

def insertdata(request):
    if request.method=='POST':
        form=project(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('insert successful')
    else:
        form=project()
        return render(request,'content.html',{'form':form})

def display(request):
    s=project.objects.all()
    res="<table border='2'><tr><th>pid</th><th>name</th><th>language</th><th>duration</th></tr>"
    for x in s:
        res+="<tr><td>"+x.pid+"</td><td>"+x.name+"</td><td>"+x.language+"</td><td>"+str(x.dutration)+"</td></tr>"
    res+="</table>"
    return HttpResponse(res)