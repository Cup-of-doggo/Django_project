from django.shortcuts import render

from catalog.models import Product

from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView


class HomeView(TemplateView):
    template_name = 'catalog/home.html'


class ContactsView(TemplateView):
    template_name = 'catalog/contacts.html'


def product_view(request):
    return render(request, 'catalog/product.html')


class ProductListView(ListView):
    model = Product
    template_name = 'catalog/product_list.html'
    context_object_name = 'products'


class ProductCreateView(CreateView):
    model = Product
    fields = ['product_name', 'description', 'category', 'price']
    template_name = 'catalog/product.html'
    success_url = reverse_lazy('catalog:product_list')


class ProductDetailView(DetailView):
    model = Product
    template_name = 'catalog/catalog_detail.html'
    context_object_name = 'product'


class ProductUpdateView(UpdateView):
    model = Product
    fields = ['product_name', 'description', 'category', 'price']
    template_name = 'catalog/product.html'
    success_url = reverse_lazy('catalog:product_list')


class ProductDeleteView(DeleteView):
    model = Product
    template_name = 'catalog/product_confirm_delete.html'
    success_url = reverse_lazy('catalog:product_list')