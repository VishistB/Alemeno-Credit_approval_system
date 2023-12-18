from django.urls import path
from . import views

urlpatterns=[
    path('',views.getEndpoints),
    path('register/', views.register, name='register'),
    path('check-eligibility/', views.check_eligibility, name='check-eligibility'),
    path('view-loan/<int:loan_id>/', views.view_loan_details, name='view_loan_details'),
    path('view-loans/<int:customer_id>/', views.view_loans_by_customer, name='view_loans_by_customer'),
    path('create-loan/', views.create_loan, name='create_loan'),
]