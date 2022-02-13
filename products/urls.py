from django.urls import path
from . import views

urlpatterns = [
    path('products/', views.all_products, name='products'),
    path('wines/', views.all_wines, name='wines'),
    path('varietals/', views.varietals, name='varietals'),
    path('<int:product_id>/', views.wine_detail, name='wine_detail'),
    path('add/', views.add_product, name='add_product'),
]