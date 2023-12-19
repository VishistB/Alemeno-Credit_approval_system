import pandas as pd
import os
import django
from django.utils import timezone

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'creditbackend.settings')
django.setup()

from api.models import LoanModel

def import_loans_from_excel(file_path):
    df = pd.read_excel(file_path)

    for _, row in df.iterrows():
        LoanModel.objects.create(
            customer_id=row['Customer ID'],
            loan_id=row['Loan ID'],
            loan_amount=row['Loan Amount'],
            tenure=row['Tenure'],
            interest_rate=row['Interest Rate'],
            monthly_repayment=row['Monthly payment'],
            emis_paid_on_time=row['EMIs paid on Time'],
            start_date=row['Date of Approval'],
            end_date=row['End Date']
        )

if __name__ == "__main__":
    excel_file_path = 'initial_data/loan_data.xlsx'

    import_loans_from_excel(excel_file_path)
