"""
URL configuration for ProductManagement project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from decouple import config
from django.contrib import admin
from django.urls import path, include
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView

class CustomSpectacularAPIView(SpectacularAPIView):
    def get(self, request, *args, **kwargs):
        response = super().get(request, *args, **kwargs)

        if not config('PROD', default=False, cast=bool):
            return response
        
        schema = response.data
        
        # Customize the paths in the schema
        modified_paths = {}
        for path, path_item in schema['paths'].items():
            modified_path = f'/production{path}'
            modified_paths[modified_path] = path_item
        
        schema['paths'] = modified_paths
        response.data = schema
        
        return response

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/product/', include('product.urls')),
    path('api/schema/', CustomSpectacularAPIView.as_view(), name='schema'),
    path('api/schema/docs/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
]
