from django.contrib import admin
from .models import Profile, MealPlan

admin.site.register(Profile)

@admin.register(MealPlan)
class MealPlanAdmin(admin.ModelAdmin):
    list_display = ('user', 'date', 'total_calories', 'diet_type', 'nutrition_goals', 'status')
    