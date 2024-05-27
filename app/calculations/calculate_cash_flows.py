def calculate_before_tax_cash_flow(noi, debt_service):
    """Calculate the before-tax cash flow."""
    return noi - debt_service

def calculate_annual_debt_service(mortgage_amount, interest_rate, loan_term):
    """Calculate the annual debt service (ADS) for a given mortgage."""
    monthly_rate = interest_rate / 12
    n_payments = loan_term * 12
    ads = (mortgage_amount * monthly_rate) / (1 - (1 + monthly_rate) ** -n_payments)
    return ads * 12

def calculate_net_operating_income(egi, operating_expenses):
    """Calculate the Net Operating Income (NOI)."""
    return egi - operating_expenses
