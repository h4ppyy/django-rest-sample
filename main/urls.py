from django.urls import path
from django.conf.urls import url, include
from rest_framework.documentation import include_docs_urls 

docs_view = include_docs_urls(
    title='rest API',
    description='simple demo',
)

urlpatterns = [
    path('docs/', docs_view),
    path('api/v1/', include('book.urls')),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
