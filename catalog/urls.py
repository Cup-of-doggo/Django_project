from django.urls import path
from . import views
from .views import catalog_detail

app_name = 'catalog'

urlpatterns = [
    path('home/', views.home, name='home'),
    path('contacts/', views.contacts, name='contacts'),
    path('product/', views.product_view, name='product'),
    path('index/', views.index, name='index'),
    path('catalog_detail/', views.catalog_detail, name='catalog_detail'),
    path('product_list/', views.product_list, name='product_list'),
]