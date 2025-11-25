from .models import Product, Category


class ProductServices:

    @staticmethod
    def get_products_by_category(category_name):
        return Product.objects.filter(category=category_name)