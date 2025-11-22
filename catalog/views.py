from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from catalog.models import Product
from catalog.forms import ProductForm


class HomeView(TemplateView):
    template_name = 'catalog/home.html'


class ContactsView(TemplateView):
    template_name = 'catalog/contacts.html'


class ProductListView(ListView):
    model = Product
    template_name = 'catalog/product_list.html'
    context_object_name = 'products'

    def get_queryset(self):
        return Product.objects.all().select_related('category')


class ProductCreateView(LoginRequiredMixin,PermissionRequiredMixin, CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'catalog/product_form.html'
    success_url = reverse_lazy('catalog:product_list')
    permission_required = 'catalog.can_unpublish_product'

    @login_required
    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)


class ProductDetailView(DetailView):
    model = Product
    template_name = 'catalog/product_detail.html'
    context_object_name = 'product'

    def get_queryset(self):
        return Product.objects.all().select_related('category')


class ProductUpdateView(LoginRequiredMixin,PermissionRequiredMixin, UpdateView):
    model = Product
    form_class = ProductForm
    template_name = 'catalog/product_form.html'
    success_url = reverse_lazy('catalog:product_list')
    permission_required = 'catalog.can_unpublish_product'

    @login_required
    def get_queryset(self):
        if not self.request.CustomUser == self.owner:
            return Product.objects.none()
        return Product.objects.all()

class ProductDeleteView(LoginRequiredMixin,PermissionRequiredMixin, DeleteView):
    model = Product
    template_name = 'catalog/catalog_confirm_delete.html'
    success_url = reverse_lazy('catalog:product_list')
    permission_required = 'catalog.delete_product'

    @login_required
    def get_queryset(self):
        if not self.request.user.has_perm('catalog.delete_product') or not self.request.CustomUser == self.owner:
            return Product.objects.none()
        return Product.objects.all()