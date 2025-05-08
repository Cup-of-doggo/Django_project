from django.shortcuts import render

from catalog.models import Product


def home(request):
    return render(request, 'catalog/home.html')


def contacts(request):
    return render(request, 'catalog/contacts.html')


def product_view(request):
    return render(request, 'catalog/product.html')


def index(request):
    product = Product.objects.get(id=1)
    context = {
        'product_name': product.product_name,
        'description': product.description,
        'category': product.category,
        'price': product.price,
    }
    return render(request, 'catalog/index.html', context=context)


def catalog_detail(request):
    product = Product.objects.get(id=1)
    context = {
        'product': product
    }
    return render(request, 'catalog/catalog_detail.html', context=context)


def product_list(request):
    products = Product.objects.all()
    context = {
        'products': products,
    }
    return render(request, 'catalog/product_list.html', context=context)
