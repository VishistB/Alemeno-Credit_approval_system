from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import CustomerModel,LoanModel
from .serializers import CustomerSerializer
from scripts.eligibile import creditScore,calculate_monthly_installment
from scripts.repayments import calculate_repayments_left

@api_view(['POST'])
def register(request):
    if request.method=='POST':
        data=request.data
        monthly_salary=data['monthly_income']

        approved_limit=round(36*monthly_salary/100000)*100000
        customer_data= {
            'first_name': data['first_name'],
            'last_name': data['last_name'],
            'age': data['age'],
            'monthly_income': monthly_salary,
            'approved_limit': approved_limit,
            'phone_number': data['phone_number'],
        }

        serializer=CustomerSerializer(data=customer_data)
        if serializer.is_valid():
            serializer.save()

            response_data= {
                'customer_id': serializer.data['customer_id'],
                'name': f"{serializer.data['first_name']} {serializer.data['last_name']}",
                'age': serializer.data['age'],
                'monthly_income': serializer.data['monthly_income'],
                'approved_limit': serializer.data['approved_limit'],
                'phone_number': serializer.data['phone_number'],
            }
            return Response(response_data,status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    

@api_view(['POST'])
def check_eligibility(request):
    if request.method=='POST':
        data = request.data
        customer_id = data['customer_id']
        loan_amount = data['loan_amount']
        interest_rate = data['interest_rate']
        tenure = data['tenure']

        try:
            customer = CustomerModel.objects.get(customer_id=customer_id)

        except CustomerModel.DoesNotExist:
            return Response({'error': 'Customer not found'}, status=status.HTTP_404_NOT_FOUND)

        credit_score = creditScore(customer,LoanModel)

        approval=False
        if credit_score>50:
            approval=True
        elif credit_score<50 and credit_score>30:
            if interest_rate>12:
                corrected_interest_rate=interest_rate
            else:
                corrected_interest_rate=12
            approval=True
        elif credit_score<30 and credit_score>10:
            if interest_rate>16:
                corrected_interest_rate=interest_rate
            else:
                corrected_interest_rate=16
            approval=True
        else:
            return Response({"Approval":"Denied"})
        
        monthly_installment=calculate_monthly_installment(loan_amount,interest_rate,tenure)
        response_data= {
            'customer_id': customer_id,
            'approval': approval,
            'interest_rate': interest_rate,
            'corrected_interest_rate': corrected_interest_rate,
            'tenure': tenure,
            'monthly_installment': monthly_installment,
        }

        return Response(response_data, status=status.HTTP_200_OK)
    

@api_view(['GET'])
def view_loan_details(request, loan_id):
    try:
        loan = LoanModel.objects.get(id=loan_id)
    except LoanModel.DoesNotExist:
        return Response({'error': 'Loan not found'}, status=status.HTTP_404_NOT_FOUND)

    customer = loan.customer
    customer_data = CustomerSerializer(customer).data

    response_data = {
        'loan_id': loan.id,
        'customer': customer_data,
        'loan_approved': loan.approved,
        'interest_rate': loan.interest_rate,
        'monthly_installment': loan.monthly_installment,
        'tenure': loan.tenure,
    }

    return Response(response_data, status=status.HTTP_200_OK)

@api_view(['GET'])
def view_loans_by_customer(request, customer_id):
    try:
        customer = CustomerModel.objects.get(id=customer_id)
    except CustomerModel.DoesNotExist:
        return Response({'error': 'Customer not found'}, status=status.HTTP_404_NOT_FOUND)

    loans = LoanModel.objects.filter(customer=customer)
    loan_data = []

    for loan in loans:
        repayments_left = calculate_repayments_left(loan.tenure, loan.paid_installments)
        loan_data.append({
            'loan_id': loan.id,
            'loan_approved': loan.approved,
            'interest_rate': loan.interest_rate,
            'monthly_installment': loan.monthly_installment,
            'repayments_left': repayments_left,
        })

    return Response(loan_data, status=status.HTTP_200_OK)