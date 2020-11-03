from django.urls import path
from django.conf.urls import url, include


urlpatterns = [
    path('api/v1/', include('book.urls')),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
