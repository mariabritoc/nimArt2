from django import forms
from .models import Contacto, Producto
from django.contrib.auth.forms import UserCreationForm
##from django.contrib.auth.models import User

class ContactoForm(forms.ModelForm):

    class Meta:
        model = Contacto
        #fields = ["nombre", "correo", "telefono", "asunto", "mensaje"]
        fields = '__all__'


class ProductoForm(forms.ModelForm):

    class Meta:
        model = Producto
        fields = '__all__'

        widgets = {
            "fecha_fabricacion": forms.SelectDateWidget(),
        }

class CustomUserCreationForm(UserCreationForm):
    pass
    ##class Meta:
       ## model = User
      ##  fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']
    