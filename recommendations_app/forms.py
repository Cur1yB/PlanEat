from .models import MealPlan, UserPreferences
from django import forms

class UserSettingsForm(forms.ModelForm):
    class Meta:
        model = MealPlan
        fields = ['diet_type', 'nutrition_goals', 'gym_sessions_count']
        widgets = {
            'diet_type': forms.Select(choices=[('vegan', 'Веганское'), ('keto', 'Кето'), ('gluten_free', 'Безглютеновое'), ('none', 'Не указано')]),
            'nutrition_goals': forms.TextInput(),
            'gym_sessions_count': forms.CheckboxInput(),
        }

    def __init__(self, *args, **kwargs):
        super(UserSettingsForm, self).__init__(*args, **kwargs)
        self.fields['gym_sessions_count'].required = False
        
class UserPreferencesForm(forms.ModelForm):
    class Meta:
        model = UserPreferences
        fields = ['show_steps_count', 'show_gym_sessions', 'show_diet_type', 
                  'show_notes', 'show_nutrition_goals', 'show_status']

class MealPlanForm(forms.ModelForm):
    class Meta:
        model = MealPlan
        labels = {
            'date': 'Дата',
            'dishes': 'Блюда',
            'total_calories': 'Общая калорийность',
            'notes': 'Заметки',
            'steps_count': 'Количество шагов в сутки',
            'gym_sessions_count': 'Количество занятий в спортзале',
            'gym_sessions_duration': 'Продолжительность одного занятия',
            'diet_type': 'Тип диеты',
            'nutrition_goals': 'Цели питания',
            'status': 'Статус',
        }
        status = forms.ChoiceField(choices=MealPlan.STATUS_CHOICES)
        fields = ['date', 'dishes', 'total_calories', 'notes', 'steps_count', 'gym_sessions_count', 'gym_sessions_duration', 'diet_type', 'nutrition_goals', 'status']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
            'dishes': forms.CheckboxSelectMultiple(),
            'total_calories': forms.NumberInput(attrs={'step': '0.01'}),
            'diet_type': forms.Select(choices=[('none', 'Не указано'), ('vegan', 'Веганское'), ('keto', 'Кето'), ('gluten_free', 'Безглютеновое'),]),
            'nutrition_goals': forms.TextInput(),
            'gym_sessions_count': forms.NumberInput(),
            'gym_sessions_duration': forms.NumberInput(),
            'status': forms.TextInput()
        }
