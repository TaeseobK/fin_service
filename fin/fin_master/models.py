from django.db import models
from fin.config import BaseModel

# Create your models here.
class Coa(BaseModel):
    name = models.CharField(max_length=64, null=True, blank=True)
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

class BudgetClass(BaseModel):
    coa = models.ManyToManyField('Coa', related_name='coas')
    company = models.IntegerField()
    unit = models.IntegerField()

    code = models.CharField(max_length=24, unique=True)
    description = models.TextField(null=True, blank=True)

    parent = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True, related_name='children')

    class Meta:
        db_table = 'budget_class'
        managed = True
        verbose_name_plural = 'BudgetClasses'
        indexes = [
            models.Index(fields=['company']),
            models.Index(fields=['unit']),
            models.Index(fields=['parent'])
        ]
    
    def __str__(self):
        return f"{self.code} - {self.description}"

class AnnualBudget(BaseModel):
    budget = models.ForeignKey('BudgetClass', on_delete=models.CASCADE, related_name='budget_class', db_index=True)
    value = models.DecimalField(max_digits=16, decimal_places=2)
    year = models.IntegerField()

    parent = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True, related_name='children')

    class Meta:
        db_table = 'annual_budget'
        managed = True
        verbose_name_plural = 'AnnualBudgets'
        indexes = [
            models.Index(fields=['budget']),
            models.Index(fields=['parent'])
        ]
    
    def __str__(self):
        return f"Annual: {self.budget.code}, {self.value}"

class MonthlyBudget(BaseModel):
    annuals = models.ManyToManyField('AnnualBudget', related_name='annuals', db_index=True)
    description = models.TextField(null=True, blank=True)
    month = models.IntegerField()
    value = models.DecimalField(max_digits=16, decimal_places=2)

    parent = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True, related_name='children', db_index=True)

    class Meta:
        db_table = 'monthyly_budget'
        managed = True
        verbose_name_plural = 'MonthlyBudgets'
        indexes = [
            models.Index(fields=['parent'])
        ]