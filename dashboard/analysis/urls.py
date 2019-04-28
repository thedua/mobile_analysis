from django.contrib import admin
from django.urls import path,include
from django.conf.urls import url
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions
from django.conf import settings
from django.conf.urls.static import static

schema_view = get_schema_view(
	openapi.Info(
		title = "My Machine Learning API",
		default_version = 'v1',
		description = "ML Problem Statement:Predicting Term Deposit Suscriptions.\n Author:Ranjith Kumar Sangi",
		),
		public = True,
		permission_classes = (permissions.AllowAny,),
    )

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/',include('prediction.urls')),
    path('dashboard/',include('dashboard.urls')),
    path('',include('project.urls')),
	url(r'^swagger(?P<format>\.json|\.yaml)$',schema_view.without_ui(cache_timeout=None),name='schema-json'),
	url(r'^swagger/$',schema_view.with_ui('swagger',cache_timeout=None),name='schema-swagger-ui'),
    url(r'^redoc/$',schema_view.with_ui('redoc',cache_timeout=None),name='schema-redoc'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
