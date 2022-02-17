from django.urls import path
from . import views

urlpatterns = [
    path('products/', views.all_products, name='products'),
    path('wines/', views.all_wines, name='wines'),
    path('varietals/', views.varietals, name='varietals'),
    # from Code Institute, force Django to interpret product id as int, not str
    path('<int:product_id>/', views.wine_detail, name='wine_detail'),
    path('add/', views.add_wine, name='add_wine'),
    path('edit/<int:product_id>/', views.edit_wine, name='edit_wine'),
    path('delete/<int:product_id>/', views.delete_wine, name='delete_wine'),
]