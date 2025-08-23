from django.db import models
from fin.config import BaseModel
import calendar

# Create your models here.
class Coa(BaseModel):
    name = models.CharField(max_length=64)
    code = models.CharField(max_length=24, unique=True)

    description = models.TextField(null=True, blank=True)

    parent = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True, related_name='children', db_index=True)

    class Meta:
        db_table = 'coas'
        managed = True
        verbose_name_plural = 'Coas'
        indexes = [
            models.Index(fields=['parent'])
        ]

    def __str__(self):
        return f"{self.code} - {self.description}"
    
class Product(BaseModel):
    name = models.CharField(max_length=64)
    code = models.CharField(max_length=24, unique=True)

    unit_id = models.IntegerField(db_index=True)

    parent = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True, db_index=True, related_name='children')
    class Meta:
        db_table = 'products'
        managed = True
        verbose_name_plural = 'Products'
        indexes = [
            models.Index(fields=['unit_id']),
            models.Index(fields=['parent'])
        ]
    
    def __str__(self):
        return f"{self.name} - {self.code}"

class BudgetCode(BaseModel):
    coas = models.ManyToManyField('Coa', related_name='coas')
    name = models.CharField(max_length=64, blank=True, null=True)
    code = models.CharField(max_length=24, unique=True)

    description = models.TextField(null=True, blank=True)

    parent = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True, related_name='children', db_index=True)

    class Meta:
        db_table = 'budget_code'
        managed = True
        verbose_name_plural = 'code_budgets'
        indexes = [
            models.Index(fields=['parent'])
        ]
    
    def __str__(self):
        return f"{self.name} - {self.code}"

class BudgetCompanies(BaseModel):
    budget_code = models.ForeignKey('BudgetCode', on_delete=models.CASCADE, related_name='budget_companies', db_index=True)
    company_id = models.IntegerField(db_index=True)

    class Meta:
        db_table = 'budget_code__company'
        managed = True
        verbose_name_plural = 'budget_companies'
        indexes = [
            models.Index(fields=['budget_code', 'company_id'])
        ]

    def __str__(self):
        return f"{self.budget_code.code} - company_id: {self.company_id}"
    
class BudgetUnits(BaseModel):
    budget_code = models.ForeignKey('BudgetCode', on_delete=models.CASCADE, related_name='budget_units', db_index=True)
    unit_id = models.IntegerField(db_index=True)

    class Meta:
        db_table = 'budget_code__unit'
        managed = True
        verbose_name_plural = 'budget_units'
        indexes = [
            models.Index(fields=['budget_code', 'unit_id'])
        ]

class YearlyTarget(BaseModel):
    company_id = models.IntegerField()
    year = models.IntegerField()
    value = models.DecimalField(max_digits=16, decimal_places=2)

    class Meta:
        db_table = 'yearly_target'
        managed = True
        verbose_name_plural = 'YearlyTargets'
        indexes = [
            models.Index(fields=['year', 'company_id']),
            models.Index(fields=['company_id']),
            models.Index(fields=['year'])
        ]
    
    def __str__(self):
        return f"Target at {self.year} is on {self.value}"

class MonthlyTarget(BaseModel):
    yearly = models.ManyToManyField('YearlyTarget', related_name='year_months')
    month = models.IntegerField()
    value = models.DecimalField(max_digits=16, decimal_places=2)

    class Meta:
        db_table = 'monthly_target'
        managed = True
        verbose_name_plural = 'MonthlyTargets'
        indexes = [
            models.Index(fields=['month'])
        ]
    
    def __str__(self):
        month_name = calendar.month_name[self.month]
        return f"Target {month_name}, {self.yearly.year} is on {self.value}"
    
class UnitTarget(BaseModel):
    target_yearly = models.ForeignKey('YearlyTarget', on_delete=models.CASCADE, related_name='target_units')
    value = models.DecimalField(max_digits=16, decimal_places=2)
    unit_id = models.IntegerField()

    class Meta:
        db_table = 'target_unit'
        managed = True
        verbose_name_plural = 'TargetUnits'
        indexes = [
            models.Index(fields=['target_yearly'])
        ]
    
    def __str__(self):
        return f"Unit_id: {self.unit_id}, year: {self.target_yearly.year}, value: {self.value}"
    
class TargetProduct(BaseModel):
    units = models.ManyToManyField('UnitTarget', related_name='products')
    year = models.ForeignKey('YearlyTarget', on_delete=models.CASCADE, related_name='year_product', db_index=True)
    product = models.ForeignKey('Product', on_delete=models.CASCADE, related_name='product_target', db_index=True)
    value = models.DecimalField(max_digits=16, decimal_places=2)

    class Meta:
        db_table = 'target_product'
        managed = True
        verbose_name_plural = 'TargetProducts'
        indexes = [
            models.Index(fields=['year']),
            models.Index(fields=['product'])
        ]

    def __str__(self):
        return f"Product name: {self.product_name}, Year: {self.year.year}, Value: IDR {self.value}"

class BudgetUnitYear(BaseModel):
    unit_id = models.IntegerField(db_index=True)
    code = models.ForeignKey('BudgetCode', on_delete=models.CASCADE, related_name='budget_unit')
    year = models.ForeignKey('YearlyTarget', on_delete=models.CASCADE, related_name='year_unit')
    value = models.DecimalField(max_digits=16, decimal_places=2)

    class Meta:
        db_table = 'budget_unit_yearly'
        managed = True
        verbose_name_plural = 'BudgetYearly'
        indexes = [
            models.Index(fields=['unit_id']),
            models.Index(fields=['year'])
        ]
    
    def __str__(self):
        return f"Unit id: {self.unit_id}, Year: {self.year.year}, Value: IDR {self.value}"