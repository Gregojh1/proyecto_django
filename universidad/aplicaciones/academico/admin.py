from django.contrib import admin
from .models import cursos,docente
from django.utils.html import format_html
# Register your models here.
#admin.site.register(cursos) OTRA FORMA DE REGISTRAR

@admin.register(cursos)

class cursoadmin(admin.ModelAdmin):  #este es el modelo administrador 
    list_display = ("id", "coloreado","creditos")
    #search_fields = ("nombre","creditos")
    #list_editable =("nombre",) se pueden editar los nombres 
    list_display_links = ("coloreado",)
    list_filter = ("creditos",) #establece porque campo filtrar
    list_per_page = 15
    """fils sets crear secciones en el panel de administracion"""
    fieldsets = (
        (None, {
            "fields": ("nombre","docente")
        }), # <--- Esta coma es obligatoria para separar las secciones
        ("Advanced options", {
            "classes": ("collapse", "wide", "extrapretty"), # Corregido "classes"
            "fields": ("creditos",)
        }), # <--- Cerras la sección
    ) # <--- Cerras el fieldsets
    
    #mostrar los datos de colores 
    def coloreado(self,obj):
        return format_html('<span style="color: red;">{}</span>', obj.nombre)
    
    coloreado.short_description = "nombre del curso"
#______________________________________________________________________________________________________
#cada vez que vayas a regisrtrar un curso siempre tienes que tener un modelo abajo de como aparecera
@admin.register(docente)

class docenteAdmin(admin.ModelAdmin):
    # Aquí puedes usar los nombres de los campos que definimos: nombre, apellido, dni, sexo
    list_display = ("id", "nombre", "apellido", "dni", "sexo")
    search_fields = ("nombre", "apellido", "dni")
    list_filter = ("sexo",)
    
    def __str__(self):
        return f"{self.apellido}, {self.nombre}"