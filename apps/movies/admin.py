from django.contrib import admin
from .models import Movie, Genre  # CAMBIO


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "release_date", "duration_minutes", "is_active")
    list_filter = ("is_active", "release_date")
    search_fields = ("title",)


@admin.register(Genre)  # NUEVO
class GenreAdmin(admin.ModelAdmin):
    list_display = ("id", "name")
    search_fields = ("name",)