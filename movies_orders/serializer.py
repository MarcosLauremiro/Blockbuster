from rest_framework import serializers
from .models import MovieOrder


class MovieOrderSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    price = serializers.DecimalField(max_digits=8, decimal_places=2)
    title = serializers.CharField(source="movie.title", read_only=True)
    purchased_at = serializers.DateTimeField(read_only=True)
    purchased_by = serializers.CharField(read_only=True, source="user.email")

    def create(self, validated_data):
        return MovieOrder.objects.create(**validated_data)
