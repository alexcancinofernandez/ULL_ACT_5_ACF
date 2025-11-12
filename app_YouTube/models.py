from django.db import models

class Canal(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    fecha_creacion = models.DateField()
    suscriptores = models.IntegerField(default=0)
    url_personalizada = models.CharField(max_length=100, unique=True)
    pais = models.CharField(max_length=50)
    categoria_principal = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre


class Video(models.Model):
    id = models.AutoField(primary_key=True)
    canal = models.ForeignKey(Canal, on_delete=models.CASCADE, related_name='videos')
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField()
    duracion = models.DurationField()
    vistas = models.IntegerField(default=0)
    publico = models.BooleanField(default=True)
    url_miniatura = models.CharField(max_length=200)
    likes = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.titulo} ({self.canal.nombre})"


class Playlist(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=150)
    descripcion = models.TextField()
    fecha_creacion = models.DateField()
    publica = models.BooleanField(default=True)
    canal_creador = models.ForeignKey(Canal, on_delete=models.CASCADE, related_name='playlists')
    videos = models.ManyToManyField(Video, related_name='playlists')
    orden_videos = models.JSONField()  # usa JSONField estándar
    n_videos = models.DecimalField(max_digits=10, decimal_places=0)

    def __str__(self):
        return f"{self.nombre} - {self.canal_creador.nombre}"