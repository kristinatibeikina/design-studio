from django import forms


class RegistrationForm(forms.Form):
    full_name = forms.CharField(label='ФИО', max_length=100, required=True, widget=forms.TextInput(attrs={'placeholder': 'Ваше ФИО'}))
    username = forms.CharField(label='Логин (латиница и дефис)', max_length=30, required=True, widget=forms.TextInput(attrs={'placeholder': 'Логин'}))
    email = forms.EmailField(label='Email', required=True, widget=forms.EmailInput(attrs={'placeholder': 'example@example.com'}))
    password = forms.CharField(label='Пароль', max_length=30, required=True, widget=forms.PasswordInput(attrs={'placeholder': 'Пароль'}))
    password_confirm = forms.CharField(label='Повторите пароль', max_length=30, required=True, widget=forms.PasswordInput(attrs={'placeholder': 'Повторите пароль'}))
    agree_to_processing = forms.BooleanField(label='Согласие на обработку персональных данных', required=True)

