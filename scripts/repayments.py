def calculate_repayments_left(tenure, paid_installments):
    repayments_left=max(tenure-paid_installments,0)
    return repayments_left