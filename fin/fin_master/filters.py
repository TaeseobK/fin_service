import django_filters
from .models import *
from fin.config import *

class CoaFilter(BaseFilter):
    class Meta:
        model = Coa
        fields = []

class BudgetCodeFilter(BaseFilter):
    class Meta:
        model = BudgetCode
        fields = []

class YearlyTargetFilter(BaseFilter):
    company_id = django_filters.NumberFilter(field_name='company_id', lookup_expr='exact')
    year = django_filters.NumberFilter(field_name='year', lookup_expr='exact')
    year__gte = django_filters.NumberFilter(field_name='year', lookup_expr='gte')
    year__lte = django_filters.NumberFilter(field_name='year', lookup_expr='lte')
    value__lte = django_filters.NumberFilter(field_name='value', lookup_expr='lte')
    value__gte = django_filters.NumberFilter(field_name='value', lookup_expr='gte')
    class Meta:
        model = YearlyTarget
        fields = []

class MonthlyTargetFilter(BaseFilter):
    month = django_filters.NumberFilter(field_name='month', lookup_expr='exact')
    month__lte = django_filters.NumberFilter(field_name='month', lookup_expr='lte')
    month__gte = django_filters.NumberFilter(field_name='month', lookup_expr='gte')
    value__lte = django_filters.NumberFilter(field_name='value', lookup_expr='lte')
    value__gte = django_filters.NumberFilter(field_name='value', lookup_expr='gte')
    class Meta:
        model = MonthlyTarget
        fields = []

class UnitTargetFilter(BaseFilter):
    unit_id = django_filters.NumberFilter(field_name='unit_id', lookup_expr='exact')
    value__lte = django_filters.NumberFilter(field_name='value', lookup_expr='lte')
    value__gte = django_filters.NumberFilter(field_name='value', lookup_expr='gte')

    class Meta:
        model = UnitTarget
        fields = []

class TargetProductFilter(BaseFilter):
    product_id = django_filters.NumberFilter(field_name='product_id', lookup_expr='exact')
    value__lte = django_filters.NumberFilter(field_name='value', lookup_expr='lte')
    value__gte = django_filters.NumberFilter(field_name='value', lookup_expr='gte')
    class Meta:
        model = TargetProduct
        fields = []

class BudgetUnitYearFilter(BaseFilter):
    unit_id = django_filters.NumberFilter(field_name='unit_id', lookup_expr='exact')
    value__lte = django_filters.NumberFilter(field_name='value', lookup_expr='lte')
    value__gte = django_filters.NumberFilter(field_name='value', lookup_expr='gte')

    class Meta:
        model = BudgetUnitYear
        fields = []

CoaFilter.init_dynamic(Coa)
BudgetCodeFilter.init_dynamic(BudgetCode)