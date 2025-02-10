from django.urls import path
from . import views
from .views import custom_logout

app_name = 'trans'  # Пространство имен для приложения

urlpatterns = [
    # основные страницы
    path('', views.home, name='home'),
    path('calculator/', views.calculator, name='calculator'),
    path('result/', views.result, name='result'),

    # страницы входа
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', custom_logout, name='logout'),

    #страницы пользователей
    path('dashboard/', views.dashboard, name='dashboard'),
    path('engineer_dashboard/', views.dashboard, name='engineer_dashboard'),
    path('admin_dashboard/', views.dashboard, name='admin_dashboard'),

    #управление отчетов
    path('download_report/', views.download_report, name='download_report'),
    path('archive/', views.archive, name='archive'),
    path('report/<int:report_id>/', views.report_detail, name='report_detail'),
    path('report/<int:report_id>/download/', views.download_report, name='download_report'),
    path('report/delete/<int:report_id>/', views.delete_report, name='delete_report'),
    path('report/<int:report_id>/', views.report_detail, name='report_detail'),

]