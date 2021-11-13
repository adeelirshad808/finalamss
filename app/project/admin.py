from django.contrib import admin
from .models import Student, Assignment, Teacher, Submissions
# Register your models here.,


class SubmissionAdmin(admin.ModelAdmin):

    list_display = ['submission_file', 'submitted_by',
                    'submitted_to', 'submission_title', 'submission_date', 'submission_status', 'marks_obtained']
    list_filter = ('submission_file', 'submitted_by',
                   'submitted_to', 'submission_title', 'submission_date', 'submission_status', 'marks_obtained')


class StudentAdmin(admin.ModelAdmin):

    list_display = ['student_username', 's_full_name', ]
    list_filter = ('student_username', 's_full_name', )
    ordering = ('-student_username',)


class TeacherAdmin(admin.ModelAdmin):

    list_display = ['teacher_username', 't_full_name']
    list_filter = ('teacher_username', 't_full_name',)


class AssignmentAdmin(admin.ModelAdmin):

    list_display = ['assignment_creator',
                    'assignment_title', 'assignment_date']
    list_filter = ('assignment_creator', 'assignment_title', 'assignment_date')


admin.site.site_header = 'AMS'
admin.site.index_title = 'AMS Admin Panel'

admin.site.register(Student, StudentAdmin)
admin.site.register(Assignment, AssignmentAdmin)
admin.site.register(Teacher, TeacherAdmin)
admin.site.register(Submissions, SubmissionAdmin)
