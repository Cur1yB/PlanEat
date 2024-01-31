from django.shortcuts import render, redirect
from .models import UserPreferences, MealPlan
from .forms import UserPreferencesForm, MealPlanForm
from django.contrib.auth.decorators import login_required
@login_required
def user_preferences(request):
    try:
        preferences = request.user.userpreferences
    except UserPreferences.DoesNotExist:
        preferences = UserPreferences.objects.create(user=request.user)
    
    if request.method == 'POST':
        form = UserPreferencesForm(request.POST, instance=preferences)
        if form.is_valid():
            form.save()
            # Перенаправляем пользователя, например, на страницу dashboard
            return redirect('dashboard')
    else:
        form = UserPreferencesForm(instance=preferences)
    return render(request, 'preferences.html', {'form': form})

@login_required
def create_meal_plan(request):
    if request.method == 'POST':
        form = MealPlanForm(request.POST)
        if form.is_valid():
            meal_plan = form.save(commit=False)
            meal_plan.user = request.user
            meal_plan.save()
            form.save_m2m()  # Сохранение связанных блюд
            # Здесь можно добавить расчет калорий
            return redirect('dashboard')
    else:
        form = MealPlanForm()
    return render(request, 'meal_plan_form.html', {'form': form})

@login_required
def edit_meal_plan(request, meal_plan_id):
    meal_plan = MealPlan.objects.get(id=meal_plan_id, user=request.user)
    if request.method == 'POST':
        form = MealPlanForm(request.POST, instance=meal_plan)
        if form.is_valid():
            form.save()
            # Обновление калорий можно выполнить здесь
            return redirect('dashboard')
    else:
        form = MealPlanForm(instance=meal_plan)
    return render(request, 'meal_plan_form.html', {'form': form})