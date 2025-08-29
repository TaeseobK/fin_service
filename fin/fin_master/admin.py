from django.contrib import admin
from .models import *
from django.db.models import Field

# Register your models here.
@admin.register(Coa)
class CoaAdmin(admin.ModelAdmin):
    def get_list_display(self, request):
        list_display = [field.name for field in self.model._meta.get_fields() if isinstance(field, Field)]
        readonly_fields = ('id', )
        return list_display

@admin.register(Product)
class BudgetClassAdmin(admin.ModelAdmin):
    def get_list_display(self, request):
        list_display = [field.name for field in self.model._meta.get_fields() if isinstance(field, Field)]
        readonly_fields = ('id', )
        return list_display

@admin.register(ProductCode)
class AnnualBudgetAdmin(admin.ModelAdmin):
    def get_list_display(self, request):
        list_display = [field.name for field in self.model._meta.get_fields() if isinstance(field, Field)]
        readonly_fields = ('id', )
        return list_display

@admin.register(ProductPrincipal)
class MonthlyBudgetAdmin(admin.ModelAdmin):
    def get_list_display(self, request):
        list_display = [field.name for field in self.model._meta.get_fields() if isinstance(field, Field)]
        readonly_fields = ('id', )
        return list_display

@admin.register(UnitProduct)
class MonthlyBudgetAdmin(admin.ModelAdmin):
    def get_list_display(self, request):
        list_display = [field.name for field in self.model._meta.get_fields() if isinstance(field, Field)]
        readonly_fields = ('id', )
        return list_display

@admin.register(Budget)
class MonthlyBudgetAdmin(admin.ModelAdmin):
    def get_list_display(self, request):
        list_display = [field.name for field in self.model._meta.get_fields() if isinstance(field, Field)]
        readonly_fields = ('id', )
        return list_display

@admin.register(UnitBudget)
class MonthlyBudgetAdmin(admin.ModelAdmin):
    def get_list_display(self, request):
        list_display = [field.name for field in self.model._meta.get_fields() if isinstance(field, Field)]
        readonly_fields = ('id', )
        return list_display

@admin.register(TargetEstimation)
class MonthlyBudgetAdmin(admin.ModelAdmin):
    def get_list_display(self, request):
        list_display = [field.name for field in self.model._meta.get_fields() if isinstance(field, Field)]
        readonly_fields = ('id', )
        return list_display

# @admin.register(BudgetUnitYear)
# class MonthlyBudgetAdmin(admin.ModelAdmin):
#     def get_list_display(self, request):
#         list_display = [field.name for field in self.model._meta.get_fields() if isinstance(field, Field)]
#         readonly_fields = ('id', )
#         return list_display