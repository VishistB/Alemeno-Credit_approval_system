import pandas as pd
import os
import django
from django.db import transaction

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'creditbackend.settings')
django.setup()

from api.models import CustomerModel, LoanModel

def calculate_current_debt(customer_id):
    loans = LoanModel.objects.filter(customer_id=customer_id)
    total_debt=0
    for loan in loans:
        total_debt += (loan.tenure - loan.emis_paid_on_time) * loan.monthly_repayment
    return total_debt

@transaction.atomic
def import_customers_from_excel(file_path):
    df = pd.read_excel(file_path)

    for _, row in df.iterrows():
        customer_id=str(row['Customer ID'])
        first_name= row['First Name']
        last_name= row['Last Name']
        age= row['Age']
        phone_number= str(row['Phone Number'])
        monthly_salary= int(row['Monthly Salary'])
        approved_limit= int(row['Approved Limit'])
        current_debt= calculate_current_debt(customer_id)

        CustomerModel.objects.create(
            customer_id=customer_id,
            first_name=first_name,
            last_name=last_name,
            age=age,
            phone_number=phone_number,
            monthly_salary=monthly_salary,
            approved_limit=approved_limit,
            current_debt=current_debt
        )

if __name__ == "__main__":
    excel_file_path = 'initial_data/customer_data.xlsx'
    import_customers_from_excel(excel_file_path)