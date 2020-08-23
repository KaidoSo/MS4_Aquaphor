from django.shortcuts import render


def home(request):
    return render(request, 'home.html')


def shop(request):
    return render(request, 'shop.html')


def productPage(request):
    return render(request, 'product.html')


def contacts(request):
    return render(request, 'contacts.html')
# Create your views here.
