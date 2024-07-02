from django.contrib import admin
from django.urls import path

from myapp1.views import current
from myapp2.views import before_after
from myapp3.views import*
from myapp4.views import*
from myapp6.views import*
#from myapp8.views import insertdata,display

urlpatterns = [
    path('admin/', admin.site.urls),
    path('now',current),
    path('bf/<int:n>',before_after),
    path('list/', homefunc, name='table.html'),
    path('aboutus/', aboutus), 
    path('home/', home), 
    path('contactus/', contactus),
    path('layout/',layout),
    path('student',insertstudent),
    path('course',insertcourse),
    path('enroll/<str:s>/<str:c>',enrollment),
    path('display',display),
    #path('enterdata',insertdata),
    #path('displays',display),
]