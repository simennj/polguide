from django.db.models import QuerySet, Max, Min
from django_filters import rest_framework as filters
from rest_framework import pagination
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ReadOnlyModelViewSet

from guide.models import Product, ProductHistory, Category
from guide.serializers import ProductSerializer, ProductHistorySerializer, CategorySerializer


class ProductFilter(filters.FilterSet):
    name = filters.CharFilter(lookup_expr='icontains')
    price = filters.RangeFilter()
    volume = filters.RangeFilter()
    alcohol = filters.RangeFilter()
    alcohol_price = filters.RangeFilter()
    category = filters.ModelMultipleChoiceFilter(queryset=Category.objects.all())

    class Meta:
        model = Product
        fields = ()


class ProductPagination(pagination.PageNumberPagination):
    page_size_query_param = 'rowsPerPage'
    max_page_size = 100


class ProductViewSet(ReadOnlyModelViewSet):
    queryset = Product.objects.all().filter()
    serializer_class = ProductSerializer
    filter_class = ProductFilter
    pagination_class = ProductPagination

    @action(detail=False)
    def aggregations(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        aggregation = self.aggregate_queryset(queryset)
        return Response(aggregation)

    @staticmethod
    def aggregate_queryset(queryset: QuerySet):
        return queryset.aggregate(
            Min('price'), Max('price'),
            Min('alcohol'), Max('alcohol'),
            Min('volume'), Max('volume'),
            Min('alcohol_price'), Max('alcohol_price'),
        )


class ProductHistoryViewSet(ReadOnlyModelViewSet):
    queryset = ProductHistory.objects.all()
    serializer_class = ProductHistorySerializer


class CategoryViewSet(ReadOnlyModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    pagination_class = None
