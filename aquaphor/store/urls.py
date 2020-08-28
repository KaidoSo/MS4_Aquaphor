from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('category/<slug:category_slug>',
         views.home, name='products_by_category'),
    path('category/<slug:category_slug>/<slug:product_slug>',
         views.productPage, name='product_detail'),
    path('cart', views.cart, name='cart'),
    path('contacts/', views.contacts, name='contacts'),
    path('product/', views.productPage, name='product'),
]
