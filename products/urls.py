from django.urls import path
from . import views

urlpatterns = [
    path('products', views.all_products, name='products'),
    path('wines', views.all_wines, name='wines'),
    path('<product_id>', views.wine_detail, name='wine_detail'),
]