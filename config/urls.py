from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions


schema_view = get_schema_view(
    openapi.Info(
        title="Post API",
        default_version='v1',
        description="API for movies",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@movies.local"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    # permission_classes=[permissions.AllowAny],
)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),

    path('advantages/', include('apps.advantages.urls')),
    path('brand/', include('apps.brand.urls')),
    path('brand_info/', include('apps.brand_info.urls')),
    path('communication/', include('apps.communication.urls')),
    path('content/', include('apps.content.urls')),
    path('flavor/', include('apps.flavor.urls')),
    path('news/', include('apps.news.urls')),
    path('partners/', include('apps.partners.urls')),
    path('product/', include('apps.product.urls')),
    path('production/', include('apps.production.urls')),
    path('vacancy/', include('apps.vacancy.urls')),
    path('language/', include('apps.language.urls')),


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
