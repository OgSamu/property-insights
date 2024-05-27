def calculate_annual_rent(units, monthly_rent):
    """Calculate the annual rent for a given number of units and monthly rent per unit."""
    return units * monthly_rent * 12

def adjust_for_vacancy(annual_rent, vacancy_rate):
    """Adjust the annual rent to account for a given vacancy rate."""
    return annual_rent * (1 - vacancy_rate)

def include_other_income(adjusted_rent, other_income_percentage):
    """Include other income as a percentage of the adjusted rent."""
    return adjusted_rent * (1 + other_income_percentage)
