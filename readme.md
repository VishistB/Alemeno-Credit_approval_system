# Credit Approval System
Made for Alemeno Tech's backend assignment

## API endpoints
    - "register": "/register/"
        - registers new user

    - "check-eligibility": "/check-eligibility/"
        - checks if user eligible for loan

    - "view-loan-details": "/view-loan/<int:loan_id>/"
        - searches for loan details based on loan id in url

    - "view-loans-by-customer": "/view-loans/<int:customer_id>/"
        - searches for loan details based on customer id in url

    - "create-loans": "create-loan/"
        - Checks loan acceptance Criteria and saves loan to database