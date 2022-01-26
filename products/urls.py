from django.urls import path
from . import views

urlpatterns = [
    path('products', views.all_products, name='all_products'),
    path('wines', views.all_wines, name='wines'),
    path('<product_id>', views.wine_detail, name='wine_detail'),
]