from django.views.decorators.csrf import csrf_exempt
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.response import Response
from api_rest.models import Book,Author
from rest_framework.status import HTTP_400_BAD_REQUEST, HTTP_201_CREATED, HTTP_202_ACCEPTED, HTTP_404_NOT_FOUND, \
    HTTP_500_INTERNAL_SERVER_ERROR
from api_rest.serializers import AuthorSerializer,BookSerializer,AuthorFormatSerializer,BookFormatListSerializer
from django.db.models import F

@api_view(['GET', 'POST'])
@csrf_exempt
def author_list(request):
    if request.method == 'GET':
    	data = Author.objects.prefetch_related('book_author')
    	serializer = AuthorFormatSerializer(data,many=True)
    	return Response(serializer.data)

    elif request.method == 'POST':
        serializer = AuthorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

@api_view(['GET', 'PUT', 'DELETE'])
@csrf_exempt
def author_detail(request, pk):
    try:
        item = Author.objects.get(pk=pk)
    except Author.DoesNotExist:
        return Response(status=400)

    if request.method == 'GET':
        serializer = AuthorFormatSerializer(item)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = AuthorSerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    elif request.method == 'DELETE':
        item.delete()
        return Response(status=204)
@api_view(['GET', 'POST'])
@csrf_exempt
def book_list(request):
    if request.method == 'GET':
    	data = Book.objects.select_related('author')
    	serializer = BookFormatListSerializer(data,many=True)
    	return Response(serializer.data)

    elif request.method == 'POST':
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


@api_view(['GET', 'PUT', 'DELETE'])
@csrf_exempt
def book_detail(request, pk):
    try:
        item = Book.objects.get(pk=pk)
    except Book.DoesNotExist:
        return Response(status=400)

    if request.method == 'GET':
        serializer = BookFormatListSerializer(item)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = BookSerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    elif request.method == 'DELETE':
        item.delete()
        return Response(status=204)
