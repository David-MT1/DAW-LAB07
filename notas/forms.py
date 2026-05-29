from django import forms
from .models import Alumno, Curso, NotasAlumnosCursos

class AlumnoForm(forms.ModelForm):
    class Meta:
        model = Alumno
        fields = ['codigo', 'nombre', 'apellido', 'fecha_nacimiento', 'dni']

class CursoForm(forms.ModelForm):
    class Meta:
        model = Curso
        fields = ['codigo', 'nombre', 'profesor']

class NotasAlumnosCursosForm(forms.ModelForm):
    class Meta:
        model = NotasAlumnosCursos
        fields = ['alumno', 'curso', 'nota', 'aprobado']