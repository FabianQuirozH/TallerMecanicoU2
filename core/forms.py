from django. forms import ModelForm
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class empleadoform(ModelForm):

    class Meta:
        model = Empleado
        fields = '__all__'


class tipoempleadoform(ModelForm):

    class Meta:
        model = tipoempleado
        fields = '__all__'

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("username",  "password1", "password2")
