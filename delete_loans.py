import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'creditbackend.settings')
django.setup()

from api.models import LoanModel

def delete_all_loans():
    LoanModel.objects.all().delete()
    print("All entries in the LoanModel table have been deleted.")

if __name__ == "__main__":
    delete_all_loans()
