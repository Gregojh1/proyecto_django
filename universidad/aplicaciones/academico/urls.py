from django.contrib import admin
from django.urls import path
from aplicaciones.academico.views import CursoListView, eliminacioncurso, listdocentes
from aplicaciones.academico.views import registroedicion, registrocurso
from aplicaciones.academico.views import registrodocento, eliminaciondoceente, docenteedicion, editardocente_final
urlpatterns = [
    path("", CursoListView.as_view(), name = "gestion_cursos"),
    path("eliminacioncurso/<int:id>", eliminacioncurso, name= "eliminacioncurso"),
    # Esta es la que CARGA el formulario (necesita el ID)
    path('registroedicion/<int:id>', registroedicion, name='registroedicion'),
    path('registrocurso/', registrocurso, name='registrocurso'),
    #links docentes
    path("docentes/", listdocentes.as_view(), name= "listdocentes"),
    path("registrardocente/", registrodocento, name= "creardocente"),
    path("eliminaciondoceente/<int:id>", eliminaciondoceente, name= "eliminardocente"),
    path("docenteedicion/<int:id>", docenteedicion , name = "docenteedicion"),
    path("editardocente_final/", editardocente_final, name="editardocente_final"),
]
