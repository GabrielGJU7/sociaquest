from django.contrib import admin
from .models import Mundo, Sala

@admin.register(Mundo)
class MundoAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'tema', 'es_publico']
    list_filter = ['tema', 'es_publico']

@admin.register(Sala)
class SalaAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'mundo', 'capacidad_maxima']
    list_filter = ['mundo']