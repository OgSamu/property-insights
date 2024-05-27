from decimal import Decimal

def calculate_compounded_expense(base_value, rate, year):
    return Decimal(base_value) * (Decimal(1) + Decimal(rate)) ** year

def calculate_operating_expenses(egi, expenses, year, annual_expense_increase, property_taxes_increase_year, property_taxes_increase_percentage):
    management_fee = Decimal(egi) * Decimal(expenses['management_fee_percentage'])
    repairs_maintenance = calculate_compounded_expense(expenses['repairs_maintenance'], annual_expense_increase, year)
    salary_expense = calculate_compounded_expense(expenses['salary_expense'], annual_expense_increase, year)
    insurance_expense = calculate_compounded_expense(expenses['insurance_expense'], annual_expense_increase, year)
    
    property_taxes = Decimal(2000)  # Default property taxes for example
    if year >= property_taxes_increase_year:
        property_taxes *= (Decimal(1) + Decimal(property_taxes_increase_percentage))

    total_operating_expenses = management_fee + repairs_maintenance + salary_expense + insurance_expense + property_taxes
    detailed_expense = {
        'management_fee': float(management_fee),
        'repairs_maintenance': float(repairs_maintenance),
        'salary_expense': float(salary_expense),
        'insurance_expense': float(insurance_expense),
        'property_taxes': float(property_taxes)
    }
    return float(total_operating_expenses), detailed_expense
