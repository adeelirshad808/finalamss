from django.urls import path
from project import views
from django.contrib.auth import views as auth_view
from django.conf import settings
from django.conf.urls.static import static
from .views import AddAssignmentView

urlpatterns = [
    path('', views.index, name='index'),
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='user_login'),
    path('logout/', views.user_logout, name='user_logout'),
    path('result/', views.result, name='result'),
    # path('assignment/', views.assignment, name='assignment'),
    path('assignment_submit/', AddAssignmentView.as_view(),
         name='assignment_submit'),

    path('teacher/', views.teacher, name='teacher'),
    path('marks/', views.marks, name='marks'),
    path('teacher_all_assignments/', views.teacher_all_assignments,
         name='teacher_all_assignments'),
    path('readfile/', views.readfile, name='readfile'),
    path('create_assignment/', views.create_assignment, name='create_assignment'),
    path('check_plagirism/', views.check_plagirism, name='check_plagirism'),
    path('online_plagirism/', views.online_plagirism, name='online_plagirism'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
