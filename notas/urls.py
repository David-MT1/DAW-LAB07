from django.urls import path
from . import views

urlpatterns = [
    path('crear_alumno/', views.crear_alumno, name='crear_alumno'),
    path('listar_alumnos/', views.listar_alumnos, name='listar_alumnos'),
    path('crear_curso/', views.crear_curso, name='crear_curso'),
    path('listar_cursos/', views.listar_cursos, name='listar_cursos'),
    path('crear_nota/', views.crear_nota, name='crear_nota'),
    path('listar_notas/', views.listar_notas, name='listar_notas'),
]