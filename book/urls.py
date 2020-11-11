from django.urls import path
from django.conf.urls import url
from django.conf import settings


from book import views as bookViews


if settings.VERSION == 1:
    url = [
        path('book', bookViews.book_v1, name='book'),
    ]
elif settings.VERSION == 2:
    url = [
        path('book', bookViews.book_v2, name='book'),
    ]
elif settings.VERSION == 3:
    url = [
        path('book', bookViews.book_v3, name='book'),
    ]

urlpatterns = url  