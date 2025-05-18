from django import forms
from .models import Autor,Relato

class AutorForm(forms.ModelForm):
    class Meta:
        model = Autor #Asociamos este formulario al modelo Autor
        fields = ['nombre','email']#Campos que se mostraran en el formulario
        labels = {
            'nombre':'Nombre completo',
            'email' : 'Correo electronico'

        }

    def clean_nombre(self):
        #Validacion personalizada para el campo nombre, asegurandonos de que el nombre tenga al menos 5 caracteres
        nombre = self.cleaned_data.get('nombre','')
        if len(nombre) < 5:
            raise forms.ValidationError("El nombre debe tener al menos 5 caracteres")
        return nombre

class RelatoForm(forms.ModelForm):    
    class Meta:
        model = Relato
        fields = ['titulo','contenido','autor']
        widgets = {
            'contenido': forms.Textarea(attrs={'rows':4}),
        }
        labels = {
            'titulo':'Titulo del relato',
            'contenido':'Contenido del resumen',
            'autor':'Nombre del autor'
        }

    def clean_titulo(self):
        titulo = self.cleaned_data.get('titulo','')
        if len(titulo) > 10:
            raise forms.ValidationError("El titulo debe tener al menos 10 caracteres")
        return titulo