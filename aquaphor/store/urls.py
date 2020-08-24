from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('<slug:category_slug>', views.home, name='products_by_category'),
    path('contacts/', views.contacts, name='contacts'),
    path('product/', views.productPage, name='product'),
]
