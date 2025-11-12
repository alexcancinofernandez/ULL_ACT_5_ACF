from django.contrib import admin
from .models import Canal, Video, Playlist

@admin.register(Canal)
class CanalAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'pais', 'suscriptores', 'url_personalizada')
    search_fields = ('nombre', 'pais')

@admin.register(Video)
class VideoAdmin(admin.ModelAdmin):
    list_display = ('id', 'titulo', 'canal', 'vistas')

@admin.register(Playlist)
class PlaylistAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'canal_creador', 'n_videos')