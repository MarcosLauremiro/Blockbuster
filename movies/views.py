from rest_framework.views import APIView, Request, Response
from django.shortcuts import get_object_or_404
from .models import Movie
from .serializer import MoviesSerializer
from .permissions import MyCustomPermission
from rest_framework.pagination import PageNumberPagination
from rest_framework_simplejwt.authentication import JWTAuthentication


class MovieView(APIView, PageNumberPagination):
    permission_classes = [MyCustomPermission]
    authentication_classes = [JWTAuthentication]

    def get(self, request: Request) -> Response:
        movies = Movie.objects.all()
        result_page = self.paginate_queryset(movies, request, view=self)
        serializer = MoviesSerializer(result_page, many=True)
        return self.get_paginated_response(serializer.data)

    def post(self, request: Request) -> Response:
        serializer = MoviesSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(user=request.user)
        return Response(serializer.data, 201)


class MovieDetailViel(APIView):
    permission_classes = [MyCustomPermission]
    authentication_classes = [JWTAuthentication]

    def get(self, request: Request, movie_id: int) -> Response:
        movie = get_object_or_404(Movie, id=movie_id)
        serializer = MoviesSerializer(movie)
        return Response(serializer.data, status=200)

    def delete(self, request: Request, movie_id: int) -> Response:
        movie = get_object_or_404(Movie, id=movie_id)
        movie.delete()
        return Response(status=204)
