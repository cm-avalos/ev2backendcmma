from django.contrib import admin



# Register your models here.



from rEquipos.models import Equipos

class EquiposAdmin(admin.ModelAdmin):
    list_display = ['marca', 'modelo', 'procesador', 'grafica', 'memoria', 'tipo']

admin.site.register(Equipos, EquiposAdmin)