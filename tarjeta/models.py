from django.db import models
from django.db.models.query_utils import select_related_descend

# Create your models here.
    
class Persona(models.Model):
    nombre= models.CharField(max_length=100, verbose_name="Nombre completo", unique= True)
    seccion_electoral= models.CharField(max_length=4, verbose_name="Seccion Electoral")
    telefono= models.CharField(max_length=10, verbose_name="Telefono",null= True)
    direccion= models.CharField(max_length=80, verbose_name="Direccion",null= True)
    zona=models.CharField(max_length=2, verbose_name="Zona")
    def __str__(self):
        #utilizo la %s para darle formato a las cadenas 
        return '  %s, sección %s' %(self.nombre, self.seccion_electoral)
class Tarjeta(models.Model):
    beneficiario= models.OneToOneField(Persona, on_delete=models.CASCADE,null=False, blank=True)
    folio_tarjeta=models.IntegerField(verbose_name="folio de tarjeta", blank=True)
    beneficio=models.CharField(max_length=50)
    def __str__(self):
        #utilizo la %s para darle formato a las cadenas 
        return 'El beneficiario es %s con beneficio %s  y tarjeta numero de folio %s' %(self.beneficiario,self.beneficio,self.folio_tarjeta)