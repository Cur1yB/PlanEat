from django import forms
from django.contrib.auth.forms import UserCreationForm, SetPasswordForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={'class': 'form-input'}))

    class Meta(UserCreationForm.Meta):
        model = User
        fields = UserCreationForm.Meta.fields + ('email',)

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user
    
class ConfirmPasswordForm(SetPasswordForm):
    def __init__(self, *args, **kwargs):
        super(ConfirmPasswordForm, self).__init__(*args, **kwargs)
        # Удаляем из формы ненужное поле new_password1
        del self.fields['new_password1']

class UsernameChangeForm(forms.ModelForm):
    current_password = forms.CharField(label='Текущий пароль', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username',)

    def clean_current_password(self):
        # Проверяем текущий пароль
        current_password = self.cleaned_data['current_password']
        if not self.instance.check_password(current_password):
            raise ValidationError('Неверный пароль.')
        return current_password

    def save(self, commit=True):
        user = super().save(commit=False)
        if commit:
            user.save()
        return user

