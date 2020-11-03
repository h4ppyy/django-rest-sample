import datetime
from django.http import HttpResponse, JsonResponse
from django.db import connections
from django.conf import settings
from book.models import *


def book_list(request):
    # query
    books = Book.objects.all()
    
    # serialize
    book_list = []
    for book in books:
      book_list.append({'id': book.id, 'book_name': book.book_name, 'created_at': book.created_at})

    return JsonResponse({'result_code': 200, 'result_data': book_list})

def book_create(request):
    # parameter
    book_name = request.GET.get('book_name')

    # query
    Book(book_name=book_name, created_at=datetime.datetime.now()).save()

    return JsonResponse({'result': 200})

def book_update(request):
    # parameter
    id = request.GET.get('id')
    book_name = request.GET.get('book_name')

    # query
    book = Book.objects.get(id=id)
    book.book_name = book_name
    book.save()

    return JsonResponse({'result': 200})

def book_delete(request):
    # parameter
    id = request.GET.get('id')

    # query
    book = Book.objects.get(id=id)
    book.book_name = book_name
    book.delete()

    return JsonResponse({'result': 200})
