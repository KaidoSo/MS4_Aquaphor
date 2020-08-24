from django.shortcuts import render, get_object_or_404
from .models import Category, Product


def home(request, category_slug=None):
    category_page = None
    products = None
    if category_slug != None:
        category_page: get_object_or_404(Category, slug=category_slug)
        products = Product.objects.filter(
            category=category_page, available=True)
    else:
        products = Product.objects.all().filter(available=True)
    return render(request, 'home.html', {'category': category_page, 'products': products})


def shop(request):
    return render(request, 'shop.html')


def productPage(request):
    return render(request, 'product.html')


def contacts(request):
    return render(request, 'contacts.html')
# Create your views here.
