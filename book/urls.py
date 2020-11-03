from django.urls import path
from django.conf.urls import url

from rest_framework.routers import DefaultRouter

# from book.views import BooksViewSet

from book import views as bookViews

# router = DefaultRouter()
# router.register(r'books', BooksViewSet, basename='books')

# urlpatterns = router.urls

urlpatterns = [
    path('book/list', bookViews.book_list, name='book_list'),
    path('book/create', bookViews.book_create, name='book_create'),
] 