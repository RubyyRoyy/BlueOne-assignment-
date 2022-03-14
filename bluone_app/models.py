from django.db import models


# Create your models here.

class Employee(models.Model):
    employee_code = models.IntegerField()
    employee_name = models.CharField(max_length=100)
    birth_date = models.DateField()
    designation = models.CharField(max_length=100)
    department = models.IntegerField()
    date_of_joining = models.DateTimeField(auto_now_add=True, blank=False, editable=False)
    bank_account_number = models.BigIntegerField()
    working_days = models.IntegerField()
    no_of_leaves = models.IntegerField()
    provident_fund_number = models.IntegerField()
    fixed_annual_ctc = models.IntegerField()
    monthly_ctc = models.IntegerField()
    balance_leaves = models.IntegerField()

    # def __str__(self):
    #     self.employee_name
