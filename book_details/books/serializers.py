from rest_framework import serializers
from books.models import Book, Author, Genre, SubGenre


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        exclude = ['slug']


class SubGenreSerializer(serializers.ModelSerializer):
    genre_name = GenreSerializer(many=False)

    class Meta:
        model = SubGenre
        exclude = ['slug']


class AuthorSerializer(serializers.ModelSerializer):
    subgenre_name = SubGenreSerializer(many=False)

    class Meta:
        model = Author
        fields = '__all__'


class BookSerializer(serializers.ModelSerializer):
    author_name = AuthorSerializer(many=False)

    class Meta:
        model = Book

        fields = ['book_name', 'author_name', 'status', 'cost', 'currency', 'publish_date_time']
