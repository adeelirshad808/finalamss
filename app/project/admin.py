from django.contrib import admin
from .models import Student, Assignment, Teacher, Submissions
# Register your models here.,

admin.site.site_header = 'AMS'
admin.site.index_title = 'AMS Admin Panel'

admin.site.register(Student)
admin.site.register(Assignment)
admin.site.register(Teacher)
admin.site.register(Submissions)