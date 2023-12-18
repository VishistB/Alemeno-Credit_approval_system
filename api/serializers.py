from rest_framework import serializers
from .models import CustomerModel,LoanModel


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomerModel
        fields = ['customer_id','first_name','last_name','age','monthly_income','approved_limit','phone_number']

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = LoanModel
        fields = ['customer_id','loan_id','loan_amount','interest_rate','tenure']



