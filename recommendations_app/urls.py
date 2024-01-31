# PlanEat/recomendations_app/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('preferences/', views.user_preferences, name='preferences'),
    path('create-meal-plan/', views.create_meal_plan, name='create_meal_plan'),
    path('edit-meal-plan/<int:meal_plan_id>/', views.edit_meal_plan, name='edit_meal_plan'),
]