from rest_framework.views import APIView, Response
from .serializers import MovieSerializer, MovieOrderSerializer
from .models import Movie
from django.shortcuts import get_object_or_404
from rest_framework_simplejwt.authentication import JWTAuthentication
from .permissions import PermissionEmployee
from rest_framework.permissions import IsAuthenticatedOrReadOnly


class MovieView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [PermissionEmployee]

    def get(self, request):
        movies = Movie.objects.all()
        serializer = MovieSerializer(movies, many=True)

        return Response(serializer.data, 200)

    def post(self, request):
        serializer = MovieSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        serializer.save(user=request.user)

        return Response(serializer.data, 201)


class MovieParamView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [PermissionEmployee]

    def get(self, request, movie_id):
        movie = get_object_or_404(Movie, id=movie_id)
        serializer = MovieSerializer(movie)

        return Response(serializer.data, 200)

    def delete(self, request, movie_id):
        movie = get_object_or_404(Movie, id=movie_id)

        movie.delete()

        return Response(status=204)


class MovieOrderParamView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]

    def post(self, request, movie_id):
        movie = get_object_or_404(Movie, id=movie_id)

        serializer = MovieOrderSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        serializer.save(user=request.user, movie_id=movie_id)

        return Response(serializer.data, 201)
