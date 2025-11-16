from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser

class AbstractUserCreationForm(UserCreationForm):
    phone_number = forms.CharField(max_length=15, required=False, help_text='Введите номер телефона. Поле необязательно для заполнения')
    username = forms.CharField(max_length=50, required=True)
    email = forms.CharField(max_length=100, required=True)
    country = forms.CharField(max_length=20, required=True)

    class Meta:
        model= CustomUser
        fields = ('email', 'username', 'country', 'phone_number','password1', 'password2', 'avatar')


    def clean_phone_number(self):
        phone_number = self.cleaned_data.get('phone_number')
        if phone_number and not phone_number.isdigit():
            raise forms.ValidationError('Номер телефона должен состоять только из цифр')
        return phone_number
