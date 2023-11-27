from .models import Movie, Rating
from rest_framework import serializers


class MoviesSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(max_length=127)
    duration = serializers.CharField(max_length=10, default="", required=False)
    rating = serializers.ChoiceField(
        choices=Rating.choices, default=Rating.G
    )
    synopsis = serializers.CharField(required=False)
    added_by = serializers.CharField(read_only=True, source="user.email")

    def create(self, validated_data):
        return Movie.objects.create(**validated_data)
