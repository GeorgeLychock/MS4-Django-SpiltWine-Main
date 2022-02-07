from django.urls import path
from . import views

urlpatterns = [
    path('', views.view_cellar, name='cellar'),
    path('add/<item_id>/', views.add_to_cellar, name='add_to_cellar'),
    path('update/<item_id>/', views.update_cellar, name='update_cellar'),
    path('remove/<item_id>/', views.remove_from_cellar, name='remove_from_cellar'),
]