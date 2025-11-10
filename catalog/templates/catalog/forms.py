from django import forms
from catalog.models import Product
from django.core.exceptions import ValidationError

banned_words = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция', 'радар']


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['product_name', 'description', 'category', 'price',]

    def clean(self):
        cleaned_data = super().clean()
        product_name = cleaned_data.get('product_name')
        description = cleaned_data.get('description')

        if product_name.lower() == banned_words or description.lower() == banned_words :
            self.add_error('product_name', 'Поле содержит недопустимое значение')


    def clean_price(self):
        price = self.cleaned_data.get('price')
        if price < 0:
            raise ValidationError('цена не может быть отрицательной')
        return price


    def __init__(self, *args, **kwargs):
        super(ProductForm, self).__init__(*args, **kwargs)

        self.fields['product_name'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Введите название товара'
        })

        self.fields['description'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Напишите описание товара'
        })

        self.fields['category'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Укажите категорию товара'
        })

        self.fields['price'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Введите цену'
        })