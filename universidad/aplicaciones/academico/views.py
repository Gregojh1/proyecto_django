from django.shortcuts import render, redirect, get_object_or_404
from aplicaciones.academico.models import cursos, docente
from django.views.generic import ListView
# Create your views here.

#vista basada en funciones sirve para empezar 
"""
def home(request):
   # return HttpResponse("<h1>Hola mundo</h1>")
   cursoslistados = cursos.objects.all().order_by("nombre")
   data = {
      "titulo" : "gestion de cursos".capitalize(),
      "cursos" : cursoslistados
   }
   #cursoslistados = cursos.objects.filter(creditos__gte=10) #filtra por creditos mayores a 10 //lte igual a 10 creditos
   #cursoslistados = cursos.objects.filter(nombre = "programacion") #filtra por lo que le digas en este caso nombre
   #cursoslistados = cursos.objects.all().order_by("-nombre") ordena por nombre decreciente
   #cursoslistados = cursos.objects.all().order_by("nombre") ordena nombre ascendente
   
   #cursoslistados = cursos.objects.all()[:2] muestra de la posicion 0 a la 2
   #cursoslistados = cursos.objects.all()[2:4] muestra de la posicion 2 a la 4 
   return render(request, "gestioncursos.html", data)
   """
 #vista basada en clases es lo recomendable en django sin embargo se puede usar con funciones tambien 
class CursoListView(ListView):
   model = cursos
   template_name = "academico/gestioncursos.html"
   context_object_name = "cursos"
   
def eliminacioncurso(request, id):
   eliminacion = cursos.objects.get(id=id)
   eliminacion.delete()
   
   return redirect("/")

def registroedicion(request, id):
    curso = get_object_or_404(cursos, id=id)
    lista_cursos = cursos.objects.all() 
    return render(request, "academico/gestioncursos.html", {
        "cursos": lista_cursos, 
        "curso": curso
    })

def registrocurso(request):

    id_curso = request.POST.get('txtid') 
    nombre = request.POST['txtnombre']
    creditos = request.POST['numcreditos']
    
    if id_curso:
 
        actualizacion = cursos.objects.get(id=id_curso)
        actualizacion.nombre = nombre
        actualizacion.creditos = creditos
        actualizacion.save()
    else:

        cursos.objects.create(
            nombre=nombre, 
            creditos=creditos
        )

    return redirect('/')
#docente vistas

class listdocentes(ListView):
    model = docente
    template_name= "academico/docentes.html"
    context_object_name = "docentes"
    


def eliminaciondoceente(request,id):
    eliminacion = docente.objects.get(id=id)
    eliminacion.delete()
    
    return redirect("listdocentes")

def docenteedicion(request, id):

    profe = docente.objects.get(id=id) 
    return render(request, "academico/ediciondocente.html", {"docente": profe})

def registrodocento(request):

    id_docente = request.POST.get('txtid') 
    nombre = request.POST['txtnombre']
    apellido = request.POST['txtapellido']
    sexo= request.POST["txtsexo"]
    dni=request.POST["txtdni"]
    
    if id_docente:
 
        actualizacion = docente.objects.get(id=id_docente)
        actualizacion.nombre = nombre
        actualizacion.apellido = apellido
        actualizacion.dni= dni
        actualizacion.save()
    else:

        docente.objects.create(
            nombre=nombre, 
            apellido=apellido,
            sexo=sexo,
            dni =dni
            )

    return redirect('listdocentes') 
    
def editardocente_final(request):
    id = request.POST['txtid']
    nombre = request.POST['txtnombre']
    apellido = request.POST['txtapellido']
    sexo = request.POST['txtsexo']

    profe = docente.objects.get(id=id)
    profe.nombre = nombre
    profe.apellido = apellido
    profe.sexo = sexo
    profe.save()

    return redirect('listdocentes')