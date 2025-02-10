from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView  # Импортируем RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('trans/', include('trans.urls', namespace='trans')),  # Подключение URL-адресов приложения trans
    path('', RedirectView.as_view(url='trans/')),  # Перенаправление с корневого URL на главную страницу
]