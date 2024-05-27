def calculate_operating_ratio(oe, egi):
    """Calculate the Operating Ratio."""
    return oe / egi

def calculate_break_even_ratio(oe, ads, egi):
    """Calculate the Break-Even Ratio."""
    return (oe + ads) / egi

def calculate_debt_coverage_ratio(noi, ads):
    """Calculate the Debt Coverage Ratio."""
    return noi / ads

def calculate_loan_to_value_ratio(mortgage, market_price):
    """Calculate the Loan-to-Value (LTV) Ratio."""
    return mortgage / market_price

def calculate_cap_rate(noi, market_price):
    """Calculate the Capitalization Rate."""
    return noi / market_price

def calculate_equity_dividend_rate(btc, initial_equity):
    """Calculate the Equity Dividend Rate."""
    return btc / initial_equity
