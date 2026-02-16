from django.db import models
from .choices import sexos
# Create your models here.
class cursos(models.Model):
    nombre = models.CharField(max_length=30)
    creditos = models.PositiveIntegerField()
    docente = models.ForeignKey("docente", null= True, blank=True, on_delete=models.SET_NULL)
    
    def __str__(self):
        return f"{self.nombre} ({self.creditos} créditos)"
    
class docente(models.Model):
    nombre = models.CharField(max_length=20, verbose_name= "Nombre")
    apellido = models.CharField(max_length=20, verbose_name= "Apellido")
    dni = models.PositiveBigIntegerField(verbose_name = "Documento")
    sexo = models.CharField(max_length= 1,choices = sexos, default= "O")
    
    def __str__(self):
        return f"{self.apellido}, {self.nombre}"
    
    class Meta:
        db_table = "Docente"
        verbose_name = "docente"
        verbose_name_plural = "docentes"
        ordering = ["apellido","-nombre"]