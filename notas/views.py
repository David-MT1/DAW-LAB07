from django.shortcuts import render, redirect 
from .forms import AlumnoForm, CursoForm, NotasAlumnosCursosForm
from .models import Alumno, Curso, NotasAlumnosCursos

def crear_alumno(request):
    if request.method == 'POST':
        form = AlumnoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_alumnos') 
    else:
        form = AlumnoForm()
    return render(request, 'notas/crear_alumno.html', {'form': form})

def listar_alumnos(request):
    alumnos = Alumno.objects.all()
    return render(request, 'notas/listar_alumnos.html', {'alumnos': alumnos})  

def crear_curso(request):
    if request.method == 'POST':
        form = CursoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_cursos') 
    else:
        form = CursoForm()
    return render(request, 'notas/crear_curso.html', {'form': form})

def listar_cursos(request):
    cursos = Curso.objects.all()
    return render(request, 'notas/listar_cursos.html', {'cursos': cursos})

def crear_nota(request):
    if request.method == 'POST':
        form = NotasAlumnosCursosForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_notas') 
    else:
        form = NotasAlumnosCursosForm()
    return render(request, 'notas/crear_nota.html', {'form': form})

def listar_notas(request):
    notas = NotasAlumnosCursos.objects.all()
    return render(request, 'notas/listar_notas.html', {'notas': notas})