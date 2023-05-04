from rest_framework import serializers
from afisha.models import Movie


class MovieSerializers(serializers.ModelSerializer):
    class Meta:
        model = Movie
        # fields = 'id name rating is_hit'.split()
        fields = '__all__'
