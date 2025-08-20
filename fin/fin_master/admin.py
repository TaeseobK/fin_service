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

@admin.register(BudgetCode)
class BudgetClassAdmin(admin.ModelAdmin):
    def get_list_display(self, request):
        list_display = [field.name for field in self.model._meta.get_fields() if isinstance(field, Field)]
        readonly_fields = ('id', )
        return list_display

@admin.register(BudgetCompanies)
class AnnualBudgetAdmin(admin.ModelAdmin):
    def get_list_display(self, request):
        list_display = [field.name for field in self.model._meta.get_fields() if isinstance(field, Field)]
        readonly_fields = ('id', )
        return list_display

@admin.register(BudgetUnits)
class MonthlyBudgetAdmin(admin.ModelAdmin):
    def get_list_display(self, request):
        list_display = [field.name for field in self.model._meta.get_fields() if isinstance(field, Field)]
        readonly_fields = ('id', )
        return list_display

@admin.register(YearlyTarget)
class MonthlyBudgetAdmin(admin.ModelAdmin):
    def get_list_display(self, request):
        list_display = [field.name for field in self.model._meta.get_fields() if isinstance(field, Field)]
        readonly_fields = ('id', )
        return list_display

@admin.register(MonthlyTarget)
class MonthlyBudgetAdmin(admin.ModelAdmin):
    def get_list_display(self, request):
        list_display = [field.name for field in self.model._meta.get_fields() if isinstance(field, Field)]
        readonly_fields = ('id', )
        return list_display

@admin.register(UnitTarget)
class MonthlyBudgetAdmin(admin.ModelAdmin):
    def get_list_display(self, request):
        list_display = [field.name for field in self.model._meta.get_fields() if isinstance(field, Field)]
        readonly_fields = ('id', )
        return list_display

@admin.register(TargetProduct)
class MonthlyBudgetAdmin(admin.ModelAdmin):
    def get_list_display(self, request):
        list_display = [field.name for field in self.model._meta.get_fields() if isinstance(field, Field)]
        readonly_fields = ('id', )
        return list_display

@admin.register(BudgetUnitYear)
class MonthlyBudgetAdmin(admin.ModelAdmin):
    def get_list_display(self, request):
        list_display = [field.name for field in self.model._meta.get_fields() if isinstance(field, Field)]
        readonly_fields = ('id', )
        return list_display