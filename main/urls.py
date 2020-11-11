from django.urls import path
from django.conf.urls import url, include

from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from django.conf import settings


schema_view_v1 = get_schema_view(
   openapi.Info(
      title="Snippets API",
      default_version='v1',
      description="Test description",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True
)

schema_view_v2 = get_schema_view(
   openapi.Info(
      title="Snippets API",
      default_version='v2',
      description="Test description",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True
)

schema_view_v3 = get_schema_view(
   openapi.Info(
      title="Snippets API",
      default_version='v3',
      description="Test description",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True
)

if settings.VERSION == 1:
   url = [
      url(r'^swagger(?P<format>\.json|\.yaml)$', schema_view_v1.without_ui(cache_timeout=0), name='schema-json'),
      url(r'^swagger/$', schema_view_v1.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
      url(r'^redoc/$', schema_view_v1.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
   ]
elif settings.VERSION == 2:
   url = [
      url(r'^swagger(?P<format>\.json|\.yaml)$', schema_view_v2.without_ui(cache_timeout=0), name='schema-json'),
      url(r'^swagger/$', schema_view_v2.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
      url(r'^redoc/$', schema_view_v2.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
   ]
elif settings.VERSION == 3:
   url = [
      url(r'^swagger(?P<format>\.json|\.yaml)$', schema_view_v3.without_ui(cache_timeout=0), name='schema-json'),
      url(r'^swagger/$', schema_view_v3.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
      url(r'^redoc/$', schema_view_v3.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
   ]

urlpatterns = [
   path('api/', include('book.urls')),
]
urlpatterns += url