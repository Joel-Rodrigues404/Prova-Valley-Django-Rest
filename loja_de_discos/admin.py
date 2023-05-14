from django.contrib import admin
from .models import Disco
# Register your models here.

class DiscoAdmin(admin.ModelAdmin):
    list_display = ('id', 'titulo', 'nome_do_artista')
    list_display_links = ('id', 'titulo')
    search_fields = ('titulo','nome_do_artista',)
    list_per_page = 5
    ordering = ('titulo',)

admin.site.register(Disco, DiscoAdmin)