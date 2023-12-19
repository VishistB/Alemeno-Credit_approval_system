from django.db import models

class CustomerModel(models.Model):
    customer_id = models.CharField(max_length=20, unique=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    age=models.IntegerField()
    phone_number = models.CharField(max_length=15)
    monthly_salary = models.IntegerField()
    approved_limit = models.IntegerField()
    current_debt = models.IntegerField()

class LoanModel(models.Model):
    # customer = models.ForeignKey(CustomerModel, on_delete=models.CASCADE)
    customer_id = models.CharField(max_length=20)
    loan_id = models.CharField(max_length=20)
    loan_amount = models.IntegerField()
    tenure = models.IntegerField()
    interest_rate = models.IntegerField()
    monthly_repayment = models.IntegerField()
    emis_paid_on_time = models.IntegerField(default=0)
    start_date = models.DateField()
    end_date = models.DateField()

    class Meta:
        unique_together = ('customer_id', 'loan_id')