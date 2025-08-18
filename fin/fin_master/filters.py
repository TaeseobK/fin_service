import django_filters
from .models import *
from fin.config import *

class CoaFilter(BaseFilter):
    class Meta:
        model = Coa
        fields = []

class BudgetClassFilter(BaseFilter):
    class Meta:
        model = BudgetClass
        fields = []

class AnnualBudgetFilter(BaseFilter):
    value__gte = django_filters.NumberFilter(field_name='value', lookup_expr='gte')
    value__lte = django_filters.NumberFilter(field_name='value', lookup_expr='lte')
    
    class Meta:
        model = AnnualBudget
        fields = []

class MonthlyBudgetFilter(BaseFilter):
    value__gte = django_filters.NumberFilter(field_name='value', lookup_expr='gte')
    value__lte = django_filters.NumberFilter(field_name='value', lookup_expr='lte')

    class Meta:
        model = MonthlyBudget
        fields = []