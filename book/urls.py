from django.urls import path
from django.conf.urls import url

from rest_framework.routers import DefaultRouter

from book.views import BooksViewSet


router = DefaultRouter()
router.register(r'books', BooksViewSet, basename='books')

urlpatterns = router.urls