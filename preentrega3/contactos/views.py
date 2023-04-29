from django.shortcuts import render
from django.http import HttpResponse
from .models import Contacto, Profesor, Curso
from .forms import ContactoFormulario, ProfesorFormulario, CursoFormulario


def ver(request):
    if (request.GET['search']):
        contactos = Contacto.objects.filter(
            nombre__contains=request.GET.get('search', ''))
    else:
        contactos = Contacto.objects.all()

    profesores = Profesor.objects.all()
    cursos = Curso.objects.all()
    return render(request, 'layouts/contactos/contactos.html', {'contactos': contactos, 'profesores': profesores, 'cursos': cursos})


def crear(request):
    formulario_contacto = ContactoFormulario()
    formulario_profesor = ProfesorFormulario()
    formulario_alumno = CursoFormulario()
    return render(request, 'layouts/contactos/crear-contacto.html', {'formularioContacto': formulario_contacto, 'formularioProfesor': formulario_profesor, 'formularioCurso': formulario_alumno})


def guardar(request):
    if (request.method == 'POST'):
        formulario_contacto = ContactoFormulario(request.POST)
        formulario_profesor = ProfesorFormulario(request.POST)
        formulario_curso = CursoFormulario(request.POST)

        if formulario_contacto.is_valid:
            formulario_contacto.save()

        if formulario_profesor.is_valid:
            formulario_profesor.save()

        if formulario_curso.is_valid:
            formulario_curso.save()

            contactos = Contacto.objects.all()
            return render(request, 'layouts/contactos/contactos.html', {'contactos': contactos, 'formularioContacto': formulario_contacto})
        else:
            return render(request, 'layouts/contactos/crear-contacto.html', {'formularioContacto': formulario_contacto, 'formularioProfesor': formulario_profesor, 'formularioCurso': formulario_alumno})
