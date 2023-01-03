from django.forms import ModelForm, TextInput

from .models import Product

class ProductForm(ModelForm):
    """
    Класс - форма для создания продукта и его внесения в базу данных
    """
    class Meta:
        model = Product
        fields = ["title", 'product_num']
        widgets = {
            "title": TextInput(attrs={
            'class': 'form-control',
            'placeholder':'Введите название'
            }),
            "product_num": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Количество'
            }),
        }
