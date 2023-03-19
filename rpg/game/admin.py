from django.contrib import admin
from .models import Personaje, Equipamiento, Objeto, Caballo


class PersonajeAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'fuerza', 'destreza', 'inteligencia', 'sigilo', 'percepcion', 'persuasion', 'atletismo', 'craft')
    list_filter = ('fuerza', 'destreza', 'inteligencia', 'sigilo', 'percepcion', 'persuasion', 'atletismo', 'craft')
    search_fields = ('nombre',)


admin.site.register(Personaje, PersonajeAdmin)
admin.site.register(Objeto)
admin.site.register(Equipamiento)
admin.site.register(Caballo)
