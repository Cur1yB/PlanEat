# PlanEat/PlanEat/urls.py

from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Корневой URL, который ведет на главную страницу
    path('admin/', admin.site.urls),
    path('auth/', include('auth_app.urls')),
    path('recommendations/', include('recommendations_app.urls')),
]