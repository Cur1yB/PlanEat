from django.contrib import admin
from django.urls import path
from django.contrib.auth.views import LogoutView
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('registration/', views.registration, name='registration'),
    path('login/', views.login, name='login'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('change-username/', views.change_username, name='change_username'),
    path('change-password/', views.change_password, name='change_password'),
    path('delete-profile/', views.delete_profile, name='delete_profile'),
    path('change-username/', views.change_username, name='change_username'),
    path('preferences/', views.user_preferences, name='preferences'),
    path('create-meal-plan/', views.create_meal_plan, name='create_meal_plan'),
    path('edit-meal-plan/<int:meal_plan_id>/', views.edit_meal_plan, name='edit_meal_plan'),
    # Добавление маршрута для выхода
    path('logout/', LogoutView.as_view(next_page='/'), name='logout'),
]