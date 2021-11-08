from rest_framework import serializers

from .models import Author, Book

class NestedAuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'

class NestedBookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'


class AuthorSerializer(serializers.ModelSerializer):
    books = NestedBookSerializer(many=True, read_only=True)
    class Meta:
        model = Author
        fields = '__all__' # ['first_name', 'last_name', 'id']

class BookSerializer(serializers.ModelSerializer):
    author_detail = NestedAuthorSerializer(read_only=True, source='author')
    class Meta:
        model = Book
        fields = '__all__'