from celery import shared_task
from .models import CustomerModel, LoanModel
from .scripts.eligibile import creditScore, calculate_monthly_installment

@shared_task
def process_loan_eligibility(customer_id, loan_amount, interest_rate, tenure):
    try:
        customer = CustomerModel.objects.get(customer_id=customer_id)
    except CustomerModel.DoesNotExist:
        #customer not present in db
        return

    credit_score = creditScore(customer, LoanModel)

    approval = False
    message = "Loan not approved"
    loan_id = None
    monthly_installment = 0

    if credit_score > 50:
        approval = True
    elif 50 > credit_score > 30 and interest_rate > 12:
        approval = True
        interest_rate = min(interest_rate, 12)
    elif 30 > credit_score > 10 and interest_rate > 16:
        approval = True
        interest_rate = min(interest_rate, 16)

    if approval:
        loan = LoanModel.objects.create(
            customer=customer,
            loan_amount=loan_amount,
            interest_rate=interest_rate,
            tenure=tenure,
        )
        loan_id = loan.id
        monthly_installment = calculate_monthly_installment(loan_amount, interest_rate, tenure)
        message = "Loan approved"