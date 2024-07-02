from django.contrib import admin
from .models import Student,Course

class StudentAdmin(admin.ModelAdmin):
    list_display = ('name', 'usn')
    search_fields = ('name',)
    list_filter = ('sem',)
    ordering = ('usn',)
admin.site.register(Student,StudentAdmin)

class CourseAdmin(admin.ModelAdmin):
    list_display = ('cname', 'cid')
    search_fields = ('cid',)
   # ordering = ('cid')
admin.site.register(Course,CourseAdmin)