# apps/movies/models.py
from django.db import models

class Genre(models.Model):  # NUEVO
    name = models.CharField(max_length=100, unique=True)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name

class Movie(models.Model):
    title = models.CharField(max_length=150)
    synopsis = models.TextField(blank=True)
    release_date = models.DateField()
    duration_minutes = models.PositiveIntegerField()
    is_active = models.BooleanField(default=True)
    genres = models.ManyToManyField(Genre, related_name="movies")  # NUEVO
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["title"]
        verbose_name = "movie"
        verbose_name_plural = "movies"

    def __str__(self) -> str:
        return self.title