from django.db import models
from django.conf import settings

# Modelos de usuario

class User(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='user', on_delete=models.CASCADE)
    title = models.CharField(max_length=150)
    completed = models.BooleanField(default=False)
    created_date = models.DateTimeField(auto_now_add=True)
    upgrade_date = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-id']
    
    def __str__(self) -> str:
        return self.title

# Modelo de categorias

class Category(models.Model):
    name = models.CharField(max_length=50, verbose_name='Nombre')
    
    class Meta:
        verbose_name = 'Categoría'
        verbose_name_plural = 'Categorías'
        ordering = ['name']
    
    def __str__(self):
        return self.name

# Create your models here.

class Film(models.Model):
    title = models.CharField(max_length=50, verbose_name='Titulo')
    description = models.TextField(verbose_name='Descripción')
    publication = models.IntegerField(verbose_name='Publicación')
    genre = models.CharField(max_length=50, verbose_name='Género')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='get_films', verbose_name='Categoría')
    image = models.ImageField(upload_to='peliculas', default='imagen_default.png', verbose_name='Imgen')
    
    class Meta:
        verbose_name = 'Pelicula'
        verbose_name_plural = 'Peliculas'
        ordering = ['title']
    
    def __str__(self):
        return self.title

