from rest_framework.fields import SerializerMethodField
from rest_framework.serializers import ModelSerializer
from rest_framework import serializers

from api_rest.models import Book,Author

#formato para edicion e inserccion
class BookSerializer(ModelSerializer):
	class Meta:
		model = Book
		fields = '__all__'

class AuthorSerializer(ModelSerializer):
	class Meta:
		model = Author
		fields = '__all__'

#Formatos para proceso de informacion
class AuthorFormatSerializer(ModelSerializer):
	class Meta:
		model = Author
		fields = ('name',)


class BookFormatSerializer(ModelSerializer):
	class Meta:
		model = Book
		fields = ('title',)

class BookFormatListSerializer(ModelSerializer):
	author = AuthorFormatSerializer()
	class Meta:
		model = Book
		fields = ('title','author',)

class AuthorFormatSerializer(ModelSerializer):
	books = BookFormatSerializer(source="book_author",many=True)
	class Meta:
		model = Author
		fields = ('name','books',)