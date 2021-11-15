from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now


class Categoria(models.Model):
    name = models.CharField(max_length=20, verbose_name="Categoria")
    created = models.DateTimeField(
        auto_now_add=True, verbose_name="Fecha de Creacion ")
    updated = models.DateTimeField(
        auto_now=True, verbose_name="Actualizado el ")

    class Meta:
        verbose_name = "Categoria"
        verbose_name_plural = "Categorias"
        ordering = ('name',)

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=40, verbose_name="Titulo")
    content = models.TextField(verbose_name="Contenido")
    published = models.DateTimeField(
        auto_now_add=True, verbose_name="Fecha de Publicación")
    image = models.ImageField(
        upload_to="blog", null=True, blank=True, verbose_name="Imagen")
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, verbose_name="Autor", related_name='get_user')
    category = models.ManyToManyField(
        Categoria, verbose_name="Categoria", related_name='get_posts')
    updated = models.DateTimeField(
        auto_now=True, verbose_name="Actualizado el ")

    class Meta:
        verbose_name = "Post"
        verbose_name_plural = "Posts"
        ordering = ('-published',)

    def __str__(self):
        return self.title


# Create your models here.
