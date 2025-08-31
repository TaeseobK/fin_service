from fin.local_settings import *
from fin.config import BaseModel
from django.db import models

class Product(BaseModel):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=24, unique=True)
    image = models.ImageField(upload_to='product_images/', null=True, blank=True)

    parent = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True, related_name='children', db_index=True)
    
    class Meta:
        db_table = 'products'
        managed = True
        verbose_name_plural = 'Products'
        indexes = [
            models.Index(fields=['parent'], name='children')
        ]
        ordering = ['-id']
        
    def __str__(self):
        return f"{self.name} - {self.code}"
    
class ProductCode(BaseModel):
    code = models.CharField(max_length=24)
    product = models.ManyToManyField('Product', related_name='product_codes')
    
    class Meta:
        db_table = 'product_codes'
        managed = True
        verbose_name_plural = 'ProductCodes'
        ordering = ['-id']
    
class ProductPrincipal(BaseModel):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='product_principals')
    principal_id = models.BigIntegerField()
    
    class Meta:
        db_table = 'product_principals'
        managed = True
        verbose_name_plural = 'ProductPrincipals'
        indexes = [
            models.Index(fields=['product', 'principal_id'], name='product_principal_idx'),
            models.Index(fields=['principal_id'], name='principal_idx'),
            models.Index(fields=['product'], name='product_on_principal_idx')
        ]
        ordering = ['-id']
        
class UnitProduct(BaseModel):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='product_units')
    unit_id = models.BigIntegerField()
    
    class Meta:
        db_table = 'unit_products'
        managed = True
        verbose_name_plural = 'UnitProducts'
        indexes = [
            models.Index(fields=['product', 'unit_id'], name='product_unit_idx'),
            models.Index(fields=['unit_id'], name='unit_idx'),
            models.Index(fields=['product'], name='product_on_unit_idx')
        ]
        ordering = ['-id']
        
class Coa(BaseModel):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=24, unique=True)
    
    parent = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True, related_name='children', db_index=True)
    
    class Meta:
        db_table = 'coas'
        managed = True
        verbose_name_plural = 'Coas'
        indexes = [
            models.Index(fields=['parent'], name='coa_parent_idx')
        ]
        ordering = ['-id']

class Budget(BaseModel):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=24, unique=True)
    description = models.TextField(null=True, blank=True)
    coa = models.ManyToManyField('Coa', related_name='budgets')
    
    class Meta:
        db_table = 'budgets'
        managed = True
        verbose_name_plural = 'Budgets'
        ordering = ['-id']
        
class UnitBudget(BaseModel):
    unit_id = models.BigIntegerField()
    budget = models.ForeignKey('Budget', on_delete=models.CASCADE, related_name='unit_budgets')

    class Meta:
        db_table = 'unit_budgets'
        managed = True
        verbose_name_plural = 'UnitBudgets'
        indexes = [
            models.Index(fields=['unit_id', 'budget'], name='unit_budget_idx'),
            models.Index(fields=['unit_id'], name='unit_on_budget_idx'),
            models.Index(fields=['budget'], name='budget_idx')
        ]
        ordering = ['-id']

class TargetEstimation(BaseModel):
    product = models.ForeignKey('Product', on_delete=models.CASCADE, related_name='target_estimations')
    unit_id = models.BigIntegerField()
    avg_3_months = models.DecimalField(max_digits=12, decimal_places=2, null=True, blank=True)
    quantity = models.DecimalField(max_digits=12, decimal_places=2, null=True, blank=True)
    hna = models.DecimalField(max_digits=12, decimal_places=2, null=True, blank=True)
    
    disc_on_fkt = models.DecimalField(max_digits=4, decimal_places=4, null=True, blank=True)
    value_disc = models.DecimalField(max_digits=12, decimal_places=2, null=True, blank=True)
    
    class Meta:
        db_table = 'target_estimations'
        managed = True
        verbose_name_plural = 'TargetEstimations'
        indexes = [
            models.Index(fields=['product', 'unit_id'], name='product_unit_target_idx'),
            models.Index(fields=['unit_id'], name='unit_target_idx'),
            models.Index(fields=['product'], name='product_target_idx')
        ]
        ordering = ['-id']