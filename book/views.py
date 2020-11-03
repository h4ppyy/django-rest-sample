import json
import datetime

from django.db import connections
from django.conf import settings
from django.http import HttpResponse, JsonResponse

from rest_framework.decorators import api_view

from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema

from book.models import *
from book.serializers import BookSerializer


@api_view(['GET'])
def book_list(request):
    # query
    books = Book.objects.all()
    
    # serialize
    serializer = BookSerializer(books, many=True)
    book_list = serializer.data

    return JsonResponse({'result_code': 200, 'result_data': book_list})


@swagger_auto_schema(
    methods=['post'], 
    request_body=BookSerializer, 
    responses={
        200: openapi.Response('hello world', BookSerializer)
    }
)
@api_view(['POST'])
def book_create(request):
    # parameter
    book_name = request.data['book_name']

    # query
    Book(book_name=book_name, created_at=datetime.datetime.now()).save()

    return JsonResponse({'result': 200})


'''
class BooksViewSet(viewsets.ViewSet):

    serializer_class = BookSerializer

    def list(self, request, format=None):
        # query
        books = Book.objects.all()
        
        # serialize
        serializer = BookSerializer(books, many=True)
        book_list = serializer.data

        return Response({'result_code': 200, 'result_data': book_list})

    def retrieve(self, request, pk=None):
        # query
        book = Book.objects.get(id=pk)
        
        # serialize
        serializer = BookSerializer(book)
        book_data = serializer.data

        return Response({'result_code': 200, 'result_data': book_data})

    # test_param = openapi.Parameter(
    #     'test', 
    #     openapi.IN_BODY, 
    #     description="test manual param", 
    #     type=openapi.TYPE_OBJECT
    # )
    # user_response = openapi.Response('response description', BookSerializer)
    # @swagger_auto_schema(method='post', manual_parameters=[test_param], responses={200: user_response})
    @swagger_auto_schema(methods=['post'], request_body=BookSerializer)
    @api_view(['POST'])
    def create(self, request, pk=None):
        # parameter
        book_name = request.data['book_name']

        # query
        Book(book_name=book_name, created_at=datetime.datetime.now()).save()

        return Response({'result': 200})

    def update(self, request, pk=None):
        # parameters
        book_name = request.data['book_name']

        # query
        book = Book.objects.get(id=pk)
        book.book_name = book_name
        book.save()

        return Response({'result': 200})

    def destroy(self, request, pk=None):
        # query
        book = Book.objects.get(id=pk)
        book.delete()

        return Response({'result': 200})
'''