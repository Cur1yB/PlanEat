from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # Добавьте дополнительные поля, которые хотите хранить в профиле
    bio = models.TextField(max_length=500, blank=True)
    location = models.CharField(max_length=30, blank=True)
    birth_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.user.username
    
class Dish(models.Model):
    name = models.CharField(max_length=100)
    ingredients = models.TextField()
    calories = models.DecimalField(max_digits=6, decimal_places=2)
    protein = models.DecimalField(max_digits=6, decimal_places=2, verbose_name='Белки')
    fats = models.DecimalField(max_digits=6, decimal_places=2, verbose_name='Жиры')
    carbohydrates = models.DecimalField(max_digits=6, decimal_places=2, verbose_name='Углеводы')
    fiber = models.DecimalField(max_digits=6, decimal_places=2, verbose_name='Клетчатка')
    sugar = models.DecimalField(max_digits=6, decimal_places=2, verbose_name='Сахара')
    sodium = models.DecimalField(max_digits=6, decimal_places=2, verbose_name='Натрий')

    def __str__(self):
        return self.name
    
    
class MealPlan(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField()
    dishes = models.ManyToManyField(Dish)
    total_calories = models.DecimalField(max_digits=6, decimal_places=2, verbose_name='Общая калорийность')
    # Время приемов пищи
    breakfast_time = models.TimeField(null=True, blank=True, verbose_name='Время завтрака')
    lunch_time = models.TimeField(null=True, blank=True, verbose_name='Время обеда')
    dinner_time = models.TimeField(null=True, blank=True, verbose_name='Время ужина')
    snack_times = models.TextField(null=True, blank=True, verbose_name='Время перекусов')
    # Заметки
    notes = models.TextField(blank=True, verbose_name='Заметки')
    steps_count = models.IntegerField(verbose_name='Количество шагов')
    gym_sessions_count = models.IntegerField(default=0, verbose_name='Количество занятий в спортзале')
    gym_sessions_duration = models.DurationField(verbose_name='Общее время занятий в спортзале')
    diet_type = models.CharField(max_length=50, blank=True, verbose_name='Тип диеты') # Типа вегетарианское, кето, безглютеновое
    nutrition_goals = models.CharField(max_length=100, blank=True, verbose_name='Цели питания')
    status = models.CharField(max_length=50, blank=True, verbose_name='Статус плана')
    
    def __str__(self):
        return f"План питания пользователя {self.user.username} на {self.date}"

class UserPreferences(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    show_steps_count = models.BooleanField(default=True, verbose_name='Показывать количество шагов')
    show_gym_sessions = models.BooleanField(default=True, verbose_name='Показывать занятия в спортзале')
    show_diet_type = models.BooleanField(default=True, verbose_name='Показывать тип диеты')
    show_breakfast_time = models.BooleanField(default=True, verbose_name='Показывать время завтрака')
    show_lunch_time = models.BooleanField(default=True, verbose_name='Показывать время обеда')
    show_dinner_time = models.BooleanField(default=True, verbose_name='Показывать время ужина')
    show_snack_times = models.BooleanField(default=True, verbose_name='Показывать время перекусов')
    show_notes = models.BooleanField(default=True, verbose_name='Показывать заметки')
    show_nutrition_goals = models.BooleanField(default=True, verbose_name='Показывать цели питания')
    show_status = models.BooleanField(default=True, verbose_name='Показывать статус плана')

    def __str__(self):
        return f"Предпочтения пользователя {self.user.username}"



