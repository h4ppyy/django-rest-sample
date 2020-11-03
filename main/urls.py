from django.urls import path
from django.conf.urls import url, include


urlpatterns = [
    path('api/v1/', include('book.urls')),
]
