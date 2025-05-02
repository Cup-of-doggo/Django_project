from django.core.management.base import BaseCommand
from catalog.models import Product, Category

class Command(BaseCommand):
    help = 'add new products to the database'

    def handle(self, *args, **options):
        category1, _ = Category.objects.get_or_create(category_name='товары для дома',
                                           description='бытовые товары')

        products = [
            {'product_name': 'Кастрюля', 'description':'из нержавеющей стали',
             'category':category1, 'price':'5000',
             'created_at':'2025-02-05', 'updated_at':'2025-02-05'},
            {'product_name': 'стол', 'description': 'деревянный кухонный',
             'category': category1, 'price': '10000',
             'created_at': '2025-02-05', 'updated_at': '2025-02-05'},
        ]

        for product_data in products:
            product, created = Product.objects.get_or_create(**product_data)
            if created:
                self.stdout.write(self.style.SUCCESS(
                    f'product: {product.product_name} added'))
            else:
                self.stdout.write(self.style.WARNING(
                    f'product: {product.product_name} exist'))