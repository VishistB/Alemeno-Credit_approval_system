def creditScore(customer):
    # this might require heavy modification
    debt=customer.current_debt
    allowed=customer.approved_limit
    cScore=round(debt/allowed)*100
    return cScore


def calculate_monthly_installment(loan_amount, interest_rate, tenure):
    monthly_interest_rate=(interest_rate/12)/100
    numerator=loan_amount*monthly_interest_rate*(1+monthly_interest_rate)**tenure
    denominator=(1+monthly_interest_rate)**tenure-1
    monthly_installment=numerator/denominator
    return monthly_installment