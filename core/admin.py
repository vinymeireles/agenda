from django.contrib import admin
from core.models import Evento
# Register your models here.

#classe para listar no display do site admin o nome dos campos
class EventoAdmin(admin.ModelAdmin):
    list_display = ('id','titulo', 'data_evento', 'data_criacao')
    list_filter = ('usuario', 'data_evento',) #cria uma lista de filtro por : titulo ou usuario, ou outro campo da table

admin.site.register(Evento, EventoAdmin) #registrando as classes ao site admin