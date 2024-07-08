from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register('manage', views.ManageProducts, basename='manage_products')

app_name = 'product'

urlpatterns = [
    path('', include(router.urls)),
]
