from django.urls import path
from project import views
from django.contrib.auth import views as auth_view
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='index'),
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='user_login'),
    path('logout/', views.user_logout, name='user_logout'),
    path('assignment/', views.assignment, name='assignment'),
    path('teacher/', views.teacher, name='teacher'),
    path('check_plagirism/', views.check_plagirism, name='check_plagirism'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
