from django import forms
from .models import Product


class UploadProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description', 'price']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Название продукта'
            }),
            'description': forms.Textarea(attrs={
                  'class': 'form-control',
                  'placeholder': 'Описание продукта'
                }),
            'price': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Цена продукта'
            }),
        }


class FilterForm(forms.Form):
    query = forms.CharField()
