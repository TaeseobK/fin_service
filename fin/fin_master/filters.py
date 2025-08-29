import django_filters
from .models import *
from fin.config import *

class ProductFilter(BaseFilter):
    class Meta:
        model = Product
        fields = []  

class ProductCodeFilter(BaseFilter):
    class Meta:
        model = ProductCode
        fields = []
    
class ProductPrincipalFilter(BaseFilter):
    class Meta:
        model = ProductPrincipal
        fields = []

class UnitProductFilter(BaseFilter):
    class Meta:
        model = UnitProduct
        fields = []

class CoaFilter(BaseFilter):
    class Meta:
        model = Coa
        fields = []

class BudgetFilter(BaseFilter):
    class Meta:
        model = Budget
        fields = []

class UnitBudgetFilter(BaseFilter):
    class Meta:
        model = UnitBudget
        fields = []

class TargetEstimationFilter(BaseFilter):
    disc_on_fkt__lte = django_filters.NumberFilter(field_name='disc_on_fkt', lookup_expr='lte')
    disc_on_fkt_gte = django_filters.NumberFilter(field_name='disc_on_fkt', lookup_expr='gte')
    
    value_disc__lte = django_filters.NumberFilter(field_name='value_disc', lookup_expr='lte')
    value_disc__gte = django_filters.NumberFilter(field_name='value_disc', lookup_expr='gte')
    
    class Meta:
        model = TargetEstimation
        fields = []

TargetEstimationFilter.init_dynamic(TargetEstimation)
ProductPrincipalFilter.init_dynamic(ProductPrincipal)
ProductCodeFilter.init_dynamic(ProductCode)
UnitProductFilter.init_dynamic(UnitProduct)
UnitBudgetFilter.init_dynamic(UnitBudget)
ProductFilter.init_dynamic(Product)
BudgetFilter.init_dynamic(Budget)
CoaFilter.init_dynamic(Coa)