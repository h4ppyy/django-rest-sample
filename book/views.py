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


@swagger_auto_schema(
    methods=['post'], 
    tags=['my custom tag'],
    operation_summary="book summary",
    operation_description="book desc",
    deprecated=False,
    request_body=BookSerializer, 
    responses={
        200: openapi.Response('hello world', BookSerializer)
    }
)
@api_view(['POST'])
def book_v1(request):
    print('v1')
    return JsonResponse({'result': 'v1'})


@swagger_auto_schema(
    methods=['post'], 
    tags=['my custom tag'],
    operation_summary="book summary",
    operation_description="book desc",
    deprecated=False,
    request_body=BookSerializer, 
    responses={
        200: openapi.Response('hello world', BookSerializer)
    }
)
@api_view(['POST'])
def book_v2(request):
    print('v2')
    return JsonResponse({'result': 'v2'})


@swagger_auto_schema(
    methods=['post'], 
    tags=['my custom tag'],
    operation_summary="book summary",
    operation_description="book desc",
    deprecated=False,
    request_body=BookSerializer, 
    responses={
        200: openapi.Response('hello world', BookSerializer)
    }
)
@api_view(['POST'])
def book_v3(request):
    print('v3')
    return JsonResponse({'result': 'v3'})