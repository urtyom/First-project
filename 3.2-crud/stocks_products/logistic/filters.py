from django_filters import rest_framework as filters
from logistic.models import Stock


class StockFilter(filters.FilterSet):
    products = filters.NumberFilter(field_name='positions__product')

    class Meta:
        model = Stock
        fields = ['products']
