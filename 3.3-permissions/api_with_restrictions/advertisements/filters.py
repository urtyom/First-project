from django_filters import rest_framework as filters

from advertisements.models import Advertisement


class AdvertisementFilter(filters.FilterSet):
    """Фильтры для объявлений."""

    # TODO: задайте требуемые фильтры
    created_date = filters.DateFromToRangeFilter(
        field_name="created_at",
        lookup_expr='date'
    )

    class Meta:
        model = Advertisement
        fields = ['created_date', 'status']
