import json
import datetime
from django.db import connections
from django.conf import settings

from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action

from book.models import *
from book.serializers import BookSerializer


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