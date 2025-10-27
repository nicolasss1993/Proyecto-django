from django.contrib import admin
from .models import Estudiante


#admin.site.register(Estudiante)


@admin.register(Estudiante)
class EstudianteAdmin(admin.ModelAdmin):
    # Campos que se muestran en la lista del admin
    list_display = ('nro_estudiante', 'nombre', 'apellido', 'documento', 'nro_telefono', 'fecha_de_nacimiento', 'fecha_de_creacion')
    
    # Campos que se pueden buscar desde el buscador del admin
    search_fields = ('nombre', 'apellido', 'documento', 'nro_estudiante')
    
    # Filtros en la barra lateral derecha
    list_filter = ('fecha_de_creacion', 'fecha_de_nacimiento')
    
    # Orden por defecto
    ordering = ('nro_estudiante',)
    
    # Campos de solo lectura (por ejemplo, la fecha de creación)
    readonly_fields = ('fecha_de_creacion',)
    
    # Agrupación de campos (opcional, para que se vea más prolijo)
    fieldsets = (
        ('Datos personales', {
            'fields': ('nombre', 'apellido', 'documento', 'fecha_de_nacimiento', 'nro_telefono')
        }),
        ('Información del sistema', {
            'fields': ('nro_estudiante', 'fecha_de_creacion'),
            'classes': ('collapse',)  # esto hace que este bloque se pueda plegar
        }),
    )
