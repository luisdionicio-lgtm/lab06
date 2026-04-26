
from rest_framework import serializers
from .models import Movie, Genre  # CAMBIO

class GenreSerializer(serializers.ModelSerializer):  # NUEVO
    class Meta:
        model = Genre
        fields = ["id", "name"]
        
class MovieSerializer(serializers.ModelSerializer):
    genres = GenreSerializer(many=True, read_only=True)  # CAMBIO
    class Meta:
        model = Movie
        fields = [
            "id",
            "title",
            "synopsis",
            "release_date",
            "duration_minutes",
            "genres",  # CAMBIO
            "is_active",
            "created_at",
            "updated_at",
        ]
        read_only_fields = ["id", "created_at", "updated_at"]