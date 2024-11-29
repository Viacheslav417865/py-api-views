from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, viewsets
from .models import Genre, Actor, Movie
from rest_framework.generics import GenericAPIView
from .serializers import (GenreSerializer, ActorSerializer,
                          CinemaHallSerializer, MovieSerializer)
from .models import CinemaHall


class GenreList(APIView):
    def get(self, request):
        genres = Genre.objects.all()
        serializer = GenreSerializer(genres, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = GenreSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,
                            status=status.HTTP_201_CREATED)
        return Response(serializer.errors,
                        status=status.HTTP_400_BAD_REQUEST)


class GenreDetail(APIView):
    def get(self, request, pk):
        try:
            genre = Genre.objects.get(pk=pk)
        except Genre.DoesNotExist:
            return Response({"error": "Genre not found"},
                            status=status.HTTP_404_NOT_FOUND)
        serializer = GenreSerializer(genre)
        return Response(serializer.data)

    def put(self, request, pk):
        try:
            genre = Genre.objects.get(pk=pk)
        except Genre.DoesNotExist:
            return Response({"error": "Genre not found"},
                            status=status.HTTP_404_NOT_FOUND)
        serializer = GenreSerializer(genre, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,
                        status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk):
        try:
            genre = Genre.objects.get(pk=pk)
        except Genre.DoesNotExist:
            return Response({"error": "Genre not found"},
                            status=status.HTTP_404_NOT_FOUND)
        serializer = GenreSerializer(genre,
                                     data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,
                        status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        try:
            genre = Genre.objects.get(pk=pk)
        except Genre.DoesNotExist:
            return Response({"error": "Genre not found"},
                            status=status.HTTP_404_NOT_FOUND)
        genre.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class ActorList(GenericAPIView):
    serializer_class = ActorSerializer

    def get(self, request):
        actors = Actor.objects.all()
        serializer = self.get_serializer(actors,
                                         many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,
                            status=status.HTTP_201_CREATED)
        return Response(serializer.errors,
                        status=status.HTTP_400_BAD_REQUEST)


class ActorDetail(GenericAPIView):
    serializer_class = ActorSerializer

    def get(self, request, pk):
        try:
            actor = Actor.objects.get(pk=pk)
        except Actor.DoesNotExist:
            return Response({"error": "Actor not found"},
                            status=status.HTTP_404_NOT_FOUND)
        serializer = self.get_serializer(actor)
        return Response(serializer.data)

    def put(self, request, pk):
        try:
            actor = Actor.objects.get(pk=pk)
        except Actor.DoesNotExist:
            return Response({"error": "Actor not found"},
                            status=status.HTTP_404_NOT_FOUND)
        serializer = self.get_serializer(actor,
                                         data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,
                        status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk):
        try:
            actor = Actor.objects.get(pk=pk)
        except Actor.DoesNotExist:
            return Response({"error": "Actor not found"},
                            status=status.HTTP_404_NOT_FOUND)
        serializer = self.get_serializer(actor,
                                         data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,
                        status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        try:
            actor = Actor.objects.get(pk=pk)
        except Actor.DoesNotExist:
            return Response({"error": "Actor not found"},
                            status=status.HTTP_404_NOT_FOUND)
        actor.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class CinemaHallViewSet(viewsets.GenericViewSet):
    queryset = CinemaHall.objects.all()
    serializer_class = CinemaHallSerializer

    def list(self, request):
        cinema_halls = self.queryset
        serializer = self.get_serializer(cinema_halls,
                                         many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,
                            status=status.HTTP_201_CREATED)
        return Response(serializer.errors,
                        status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        try:
            cinema_hall = CinemaHall.objects.get(pk=pk)
        except CinemaHall.DoesNotExist:
            return Response({"error": "CinemaHall not found"},
                            status=status.HTTP_404_NOT_FOUND)
        serializer = self.get_serializer(cinema_hall)
        return Response(serializer.data)

    def update(self, request, pk=None):
        try:
            cinema_hall = CinemaHall.objects.get(pk=pk)
        except CinemaHall.DoesNotExist:
            return Response({"error": "CinemaHall not found"},
                            status=status.HTTP_404_NOT_FOUND)
        serializer = self.get_serializer(cinema_hall,
                                         data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,
                        status=status.HTTP_400_BAD_REQUEST)

    def partial_update(self, request, pk=None):
        try:
            cinema_hall = CinemaHall.objects.get(pk=pk)
        except CinemaHall.DoesNotExist:
            return Response({"error": "CinemaHall not found"},
                            status=status.HTTP_404_NOT_FOUND)
        serializer = self.get_serializer(cinema_hall,
                                         data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,
                        status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        try:
            cinema_hall = CinemaHall.objects.get(pk=pk)
        except CinemaHall.DoesNotExist:
            return Response({"error": "CinemaHall not found"},
                            status=status.HTTP_404_NOT_FOUND)
        cinema_hall.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

    def list(self, request, *args, **kwargs):
        movies = self.queryset
        serializer = self.get_serializer(movies, many=True)
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,
                            status=status.HTTP_201_CREATED)
        return Response(serializer.errors,
                        status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None, *args, **kwargs):
        try:
            movie = self.queryset.get(pk=pk)
        except Movie.DoesNotExist:
            return Response({"error": "Movie not found"},
                            status=status.HTTP_404_NOT_FOUND)
        serializer = self.get_serializer(movie)
        return Response(serializer.data)

    def update(self, request, pk=None, *args, **kwargs):
        try:
            movie = self.queryset.get(pk=pk)
        except Movie.DoesNotExist:
            return Response({"error": "Movie not found"},
                            status=status.HTTP_404_NOT_FOUND)
        serializer = self.get_serializer(movie, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,
                        status=status.HTTP_400_BAD_REQUEST)

    def partial_update(self, request, pk=None, *args, **kwargs):
        try:
            movie = self.queryset.get(pk=pk)
        except Movie.DoesNotExist:
            return Response({"error": "Movie not found"},
                            status=status.HTTP_404_NOT_FOUND)
        serializer = self.get_serializer(movie,
                                         data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,
                        status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None, *args, **kwargs):
        try:
            movie = self.queryset.get(pk=pk)
        except Movie.DoesNotExist:
            return Response({"error": "Movie not found"},
                            status=status.HTTP_404_NOT_FOUND)
        movie.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
