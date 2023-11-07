from django import forms
from .models import User, Application
from django.core.exceptions import ValidationError
import re


class Registration(forms.Form):
    full_name = forms.CharField(label='ФИО', max_length=100, required=True, widget=forms.TextInput(attrs={'placeholder': 'Ваше ФИО'}))
    username = forms.CharField(label='Логин (латиница и дефис)', max_length=30, required=True, widget=forms.TextInput(attrs={'placeholder': 'Логин'}))
    email = forms.EmailField(label='Email', required=True, widget=forms.EmailInput(attrs={'placeholder': 'example@example.com'}))
    password = forms.CharField(label='Пароль', max_length=30, required=True, widget=forms.PasswordInput(attrs={'placeholder': 'Пароль'}))
    password_confirm = forms.CharField(label='Повторите пароль', max_length=30, required=True, widget=forms.PasswordInput(attrs={'placeholder': 'Повторите пароль'}))
    agree_to_processing = forms.BooleanField(label='Согласие на обработку персональных данных', required=True)
    error_css_class = "error"
    required_css_class = "field"

    def clean_full_name(self):
        full_name = self.cleaned_data['full_name']
        if not re.match(r'^[а-яА-Я\s-]+$', full_name):
            raise ValidationError("ФИО может содержать только кириллические буквы, дефис и пробелы.")
        return full_name

    def clean_password_confirm(self):
        password = self.cleaned_data['password']
        password_confirm = self.cleaned_data['password_confirm']
        if password != password_confirm:
            self.add_error('', "Пароли не совподают!")
        return password_confirm

    def clean_username(self):
        username = self.cleaned_data['username']
        if not re.match(r'^[a-zA-Z-]+$', username):
            raise ValidationError("Логин может содержать только латиницу и дефис.")
        if User.objects.filter(username=username).exists():
            raise ValidationError("Логин не уникален.")
        return username

    class Meta:
        model = User


class LoginForm(forms.Form):
    username = forms.CharField(label='Логин (латиница и дефис)', max_length=30, required=True, widget=forms.TextInput(attrs={'placeholder': 'Логин'}))
    password = forms.CharField(label='Пароль', max_length=30, required=True, widget=forms.PasswordInput(attrs={'placeholder': 'Пароль'}))


class ChangeStatusRequest(forms.ModelForm):
    comment = forms.CharField(required=False)
    img = forms.ImageField(required=False)
    class Meta:
        model = Application
        fields = ['status', 'img', 'comment']

    def clean(self):
        cleaned_data = super().clean()
        new_status = cleaned_data.get('status')

        if new_status == 'Выполнено':
            img = cleaned_data.get('img')
            if not img:
                raise forms.ValidationError("При смене статуса на 'Выполнено' необходимо прикрепить изображение дизайна")

        if new_status == 'Принято в работу':
            comment = cleaned_data.get('comment')
            if not comment:
                raise forms.ValidationError("При смене статуса на 'Принято в работу' необходимо указать комментарий")

        return cleaned_data