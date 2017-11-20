from django import forms
from models import ClaseEstudiante
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class registroForm(UserCreationForm):
	class Meta:
		model = User 
		fields = [
			'username',
			'first_name',
			'last_name',
			'email',
		]
		labels = {
			'username': 'Nombre de usuario',
			'first_name': 'Nombre',
			'last_name': 'Apellido',
			'email': 'Correo',
		}

class ClaseEstudianteForm(forms.ModelForm):
	class Meta:
		model = ClaseEstudiante
		fields = '__all__'