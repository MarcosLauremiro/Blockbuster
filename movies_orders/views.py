from django.shortcuts import get_object_or_404
from rest_framework.views import APIView, Request, Response
from rest_framework.permissions import IsAuthenticated
from movies.models import Movie
from .models import MovieOrder
from .serializer import MovieOrderSerializer


class MovieOrderView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request: Request, movie_id: int) -> Response:
        serializer = MovieOrderSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        movie = get_object_or_404(Movie, id=movie_id)
        serializer.save(user=request.user, movie=movie)
        return Response(serializer.data, 201)
