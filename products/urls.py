from django.urls import path
from . import views

urlpatterns = [
    path('products/', views.all_products, name='products'),
    path('wines/', views.all_wines, name='wines'),
    path('varietals/', views.varietals, name='varietals'),
    # force Django to interpret product id as int, not str
    path('<int:product_id>/', views.wine_detail, name='wine_detail'),
    path('add/', views.add_product, name='add_product'),
    path('edit/<int:product_id>/', views.edit_product, name='edit_product'),
    path('delete/<int:product_id>/', views.delete_product, name='delete_product'),
]