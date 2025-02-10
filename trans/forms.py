from django import forms
from .models import Pipeline, Product, Transportation

class PipelineForm(forms.ModelForm):
    class Meta:
        model = Pipeline
        fields = ['Diameter', 'Length', 'ElevationDifference', 'ResidualHead', 'Temperature']

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['Name', 'Density293', 'Viscosity273', 'Viscosity293']

class TransportationForm(forms.ModelForm):
    class Meta:
        model = Transportation
        fields = ['PipelineID', 'ProductID', 'Quantity', 'Percentage']

from django import forms
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from .models import User

class RegisterForm(UserCreationForm):
    username = forms.CharField(max_length=150, required=True)
    surname = forms.CharField(max_length=150, required=False)
    name = forms.CharField(max_length=150, required=False)
    patronymic = forms.CharField(max_length=150, required=False)

    class Meta:
        model = User
        fields = ['username', 'surname', 'name', 'patronymic', 'password1', 'password2', 'role']

class LoginForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ['username', 'password']