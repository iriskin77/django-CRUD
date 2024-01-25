from django.shortcuts import render
from django.views import View
from django.views.generic import UpdateView, DeleteView, DetailView, CreateView
from django.urls import reverse_lazy
from django.contrib.postgres.search import SearchVector, SearchQuery, SearchRank
from .models import Product
from .forms import UploadProductForm, FilterForm


class ProductsList(View):

    """"Список товаров"""""

    template_name = 'products/list_products.html'

    def get(self, request):

        if not request.GET:
            products = Product.objects.all()
            return render(request, self.template_name, {'products': products, 'is_sorted': False})

        sorted_list = []
        sorted_params = dict(request.GET).get('sort')

        check_fields = ['name', 'price', 'date']
        for key in sorted_params:
            if key in check_fields:
                sorted_list.append(key)

        sorted_products = Product.objects.order_by(*sorted_list)

        return render(request, self.template_name, {'products': sorted_products, 'is_sorted': True})


class UpdateProduct(UpdateView):

    """"Обновление информации о товаре"""""

    model = Product
    form_class = UploadProductForm
    template_name = 'products/update_product.html'


class DetailProduct(DetailView):

    """"Подробный просмотр характеристик товара"""""

    model = Product
    template_name = 'products/product_detail.html'


class DeleteProduct(DeleteView):

    """"Удаление товара из БД"""""

    model = Product
    template_name = 'products/product_confirm_delete.html'
    context_object_name = 'product'
    success_url = reverse_lazy("list_products")


class AddProductView(CreateView):

    """"Добавление товара в БД"""""

    form_class = UploadProductForm
    template_name = 'products/add_product.html'

    def form_valid(self, form):
        return super().form_valid(form)


class ProductFilter(View):

    """"Текстовый поиск по названию и описанию товара"""""

    template = 'products/search_products.html'

    def get(self, request):

        form = FilterForm(request.GET)

        if form.is_valid():
            query = form.cleaned_data['query']
            search_vector = SearchVector('name', 'description')
            search_query = SearchQuery(query)
            found_products = Product.objects.all().\
                annotate(search=search_vector,
                         rank=SearchRank(search_vector, search_query)).\
                filter(search=search_query).order_by('-rank')

            return render(request, self.template, {'form': form, 'query': query, "found_products": found_products})

        return render(request, self.template, {'form': form})
