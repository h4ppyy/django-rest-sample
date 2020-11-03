from django.urls import path
from django.conf.urls import url

from book import views as bookViews


urlpatterns = [
    path('book/list', bookViews.book_list, name='book_list'),
    path('book/create', bookViews.book_create, name='book_create'),
    path('book/update', bookViews.book_update, name='book_update'),
    path('book/delete', bookViews.book_delete, name='book_delete'),
]