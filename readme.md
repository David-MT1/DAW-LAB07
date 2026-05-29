# Lab 07 - Sistema de Notas con Django

**Asignatura:** Laboratorio de Desarrollo de Aplicaciones Web  
**Alumno:** David Jose Luis Mendoza Taco  
**Docente:** Mc. Carlo Corrales D.  
**Año:** 2026-A

---

## Descripción

Sistema web desarrollado con Django que permite gestionar Alumnos, Cursos y Notas. Implementa el patrón MTV (Modelos - Templates - Vistas) de Django.

### Funcionalidades
- Registrar nuevos alumnos
- Registrar nuevos cursos
- Asignar notas a alumnos por curso
- Listar alumnos, cursos y notas

---

## Requisitos

- Python 3.14+
- Django 6.0+

---

## Instalación

### 1. Clonar el repositorio y entrar a la carpeta
```bash
git clone <url-del-repositorio>
cd EjerPropuesto
```

### 2. Crear y activar el entorno virtual
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
```

### 3. Instalar dependencias
```bash
pip install django
```

### 4. Aplicar migraciones
```bash
python manage.py makemigrations notas
python manage.py migrate
```

### 5. Ejecutar el servidor
```bash
python manage.py runserver
```

---

## Uso

Acceder desde el navegador a:

| URL | Descripción |
|-----|-------------|
| `/notas/crear_alumno/` | Registrar un nuevo alumno |
| `/notas/listar_alumnos/` | Ver todos los alumnos |
| `/notas/crear_curso/` | Registrar un nuevo curso |
| `/notas/listar_cursos/` | Ver todos los cursos |
| `/notas/crear_nota/` | Asignar nota a un alumno |
| `/notas/listar_notas/` | Ver todas las notas |

---

## Estructura del Proyecto

```
EjerPropuesto/
├── sistema_notas/          # Configuración del proyecto
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── notas/                  # Aplicación principal
│   ├── models.py           # Modelos: Alumno, Curso, NotasAlumnosCursos
│   ├── views.py            # Vistas
│   ├── forms.py            # Formularios
│   ├── urls.py             # URLs de la app
│   └── templates/
│       └── notas/
│           ├── crear_alumno.html
│           ├── listar_alumnos.html
│           ├── crear_curso.html
│           ├── listar_cursos.html
│           ├── crear_nota.html
│           └── listar_notas.html
├── manage.py
└── README.md
```

---

## Modelos

### Alumno
| Campo | Tipo | Descripción |
|-------|------|-------------|
| codigo | CharField | Código único del alumno |
| nombre | CharField | Nombre del alumno |
| apellido | CharField | Apellido del alumno |
| fecha_nacimiento | DateField | Fecha de nacimiento |
| dni | CharField | DNI único |

### Curso
| Campo | Tipo | Descripción |
|-------|------|-------------|
| codigo | CharField | Código único del curso |
| nombre | CharField | Nombre del curso |
| profesor | CharField | Nombre del profesor |

### NotasAlumnosCursos
| Campo | Tipo | Descripción |
|-------|------|-------------|
| alumno | ForeignKey | Relación con Alumno |
| curso | ForeignKey | Relación con Curso |
| nota | DecimalField | Nota obtenida |
| aprobado | BooleanField | Si aprobó o no |
