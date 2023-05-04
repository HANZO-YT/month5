from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from afisha.serializers import MovieSerializers
from afisha.models import Movie


@api_view(['GET'])
def movie_list_api_view(request):
    movies = Movie.objects.all()
    data_dict = MovieSerializers(movies, many=True).data
    return Response(data=data_dict)


@api_view(['GET'])
def movie_detail_api_view(request, id):
    try:
        movie = Movie.objects.get(id=id)
    except Movie.DoesNotExist:
        return Response(data={'error': 'Movie not found'},
                        status=status.HTTP_404_NOT_FOUND)
    data_dict = MovieSerializers(movie, many=False).data
    return Response(data=data_dict)


@api_view(['GET'])
def test_api_view(request):
    data_dict = {
        "text": "Hello World!",
        "int": 1000,
        "float": 9.99,
        "bool": True,
        "dict": {'key': 'value'},
        "list": [1, 2, 3]
    }
    return Response(data=data_dict)
