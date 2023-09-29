from django import forms
from .models import Persona, Parentesco, Matrimonio

class PersonaForm(forms.ModelForm):
    class Meta:
        model = Persona
        fields = ['nombre', 'fecha_nacimiento']  # Los campos que quieres mostrar en el formulario

class ParentescoForm(forms.ModelForm):
    class Meta:
        model = Parentesco
        fields = ['padre', 'hijo']  # Los campos que quieres mostrar en el formulario

class MatrimonioForm(forms.ModelForm):
    class Meta:
        model = Matrimonio
        fields = ['persona1', 'persona2']  # Los campos que quieres mostrar en el formulario
