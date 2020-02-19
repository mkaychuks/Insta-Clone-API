from django.contrib import admin
from django.urls import path, include, re_path

from rest_framework import permissions

from drf_yasg.views import get_schema_view
from drf_yasg import openapi


schema_view = get_schema_view(
   openapi.Info(
      title="Insta-Clone API",
      default_version='v1',
      description="AN INSTAGRAM CLONE API",
      contact=openapi.Contact(url='www.github.com/mkaychuks'),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('rest_auth/', include('rest_auth.urls')),
    path('signup/', include('rest_auth.registration.urls')),
    path('user/', include('users.urls')),
    path('', include('instaclone.urls')),
]

urlpatterns += [
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
