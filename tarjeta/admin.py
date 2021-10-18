from django.db import models
from import_export import resources
from import_export.admin import ImportExportActionModelAdmin, ImportExportModelAdmin

from django.contrib import admin
from django.contrib.admin.decorators import register
from django.contrib.admin.filters import ListFilter
from tarjeta.models import Persona, Tarjeta

# Register your models here.
#para utilizar el impor/export excel  inf en https://www.youtube.com/watch?v=OyVG5TWCB2s&ab_channel=Neunapp
class PersonaResources(resources.ModelResource):
    class Meta:
        model= Persona
class TarjetaResources(resources.ModelResource):
    class Meta:
        model= Tarjeta
    

class PersonaAdmin(ImportExportModelAdmin):
    resource_class=PersonaResources
    list_display=("zona","seccion_electoral","nombre","direccion","telefono")
    search_fields=("nombre",)
    list_filter=("seccion_electoral",)

class TarjetaAdmin(ImportExportModelAdmin):
    resource_class=TarjetaResources
    list_display=( "beneficiario","folio_tarjeta","beneficio")
    search_fields=("folio_tarjeta",)
    list_filter=("beneficio",)
admin.site.register(Tarjeta,TarjetaAdmin)

admin.site.register(Persona,PersonaAdmin)

