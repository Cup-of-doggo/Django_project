from django import forms
from catalog.models import Product
from django.core.exceptions import ValidationError

banned_words = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция', 'радар']

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['product_name', 'description', 'image', 'category', 'price']

    def clean_product_name(self):
        product_name = self.cleaned_data.get('product_name')
        for word in banned_words:
            if word in product_name.lower():
                raise ValidationError(f'Название содержит запрещенное слово: {word}')
        return product_name

    def clean_description(self):
        description = self.cleaned_data.get('description')
        for word in banned_words:
            if word in description.lower():
                raise ValidationError(f'Описание содержит запрещенное слово: {word}')
        return description

    def clean_price(self):
        price = self.cleaned_data.get('price')
        if price < 0:
            raise ValidationError('Цена не может быть отрицательной')
        return price

    def __init__(self, *args, **kwargs):
        super(ProductForm, self).__init__(*args, **kwargs)

        for field_name, field in self.fields.items():
            field.widget.attrs.update({
                'class': 'form-control',
                'placeholder': f'Введите {field.label.lower()}'
            })