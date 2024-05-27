from flask import Flask, render_template, request, jsonify
from calculations.calculate_rent import calculate_annual_rent, adjust_for_vacancy, include_other_income
from calculations.calculate_expenses import calculate_operating_expenses
from calculations.calculate_cash_flows import calculate_before_tax_cash_flow, calculate_annual_debt_service, calculate_net_operating_income
from calculations.calculate_ratios import calculate_operating_ratio, calculate_break_even_ratio, calculate_debt_coverage_ratio, calculate_loan_to_value_ratio, calculate_cap_rate, calculate_equity_dividend_rate

app = Flask(__name__, template_folder='../templates', static_folder='../static')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    try:

        data = request.json
        units = data['units']
        holding_period = int(data['holding_period'])
        vacancy_rate = data['vacancy_rate']
        other_income_percentage = float(data['other_income_percentage'])
        operating_expenses = float(data['operating_expenses'])
        annual_expense_increase = float(data['annual_expense_increase'])
        property_taxes_increase_year = int(data['property_taxes_increase_year'])
        property_taxes_increase_percentage = float(data['property_taxes_increase_percentage'])
        mortgage_amount = float(data['mortgage_amount'])
        interest_rate = float(data['interest_rate'])
        loan_term = int(data['loan_term'])
        management_fee_percentage = float(data['management_fee_percentage'])
        salary_expense = float(data['salary_expense'])
        insurance_expense = float(data['insurance_expense'])
        property_taxes = float(data['property_taxes'])

        # Ensure vacancy_rate has enough values
        default_vacancy_rate = vacancy_rate[-1] if vacancy_rate else 0.05  # Use the last rate or a default value
        while len(vacancy_rate) < holding_period:
            vacancy_rate.append(default_vacancy_rate)

        results = []
        for year in range(1, holding_period + 1):
            total_annual_rent = sum(calculate_annual_rent(details['units'], details['monthly_rent']) for details in units.values())
            if year > 1:
                total_annual_rent *= 1.03

            adjusted_rent = adjust_for_vacancy(total_annual_rent, vacancy_rate[year - 1])
            egi = include_other_income(adjusted_rent, other_income_percentage)

            expenses = {
                'management_fee_percentage': management_fee_percentage,
                'repairs_maintenance': operating_expenses,
                'salary_expense': salary_expense,
                'insurance_expense': insurance_expense,
                'property_taxes': property_taxes
            }

            operating_expenses_total, detailed_expense = calculate_operating_expenses(
                egi, expenses, year, annual_expense_increase, property_taxes_increase_year, property_taxes_increase_percentage
            )

            noi = calculate_net_operating_income(egi, operating_expenses_total)
            ads = calculate_annual_debt_service(mortgage_amount, interest_rate, loan_term)
            btc = calculate_before_tax_cash_flow(noi, ads)

            operating_ratio = calculate_operating_ratio(operating_expenses_total, egi)
            break_even_ratio = calculate_break_even_ratio(operating_expenses_total, ads, egi)
            debt_coverage_ratio = calculate_debt_coverage_ratio(noi, ads)
            ltv_ratio = calculate_loan_to_value_ratio(mortgage_amount, 12000000)  # Assume market price input if necessary
            cap_rate = calculate_cap_rate(noi, 12000000)  # Assume market price input if necessary
            equity_dividend_rate = calculate_equity_dividend_rate(btc, 4000000)  # Assume initial equity input if necessary

            results.append({
                'year': year,
                'noi': noi,
                'ads': ads,
                'btc': btc,
                'operating_ratio': operating_ratio,
                'break_even_ratio': break_even_ratio,
                'debt_coverage_ratio': debt_coverage_ratio,
                'ltv_ratio': ltv_ratio,
                'cap_rate': cap_rate,
                'equity_dividend_rate': equity_dividend_rate,
                'detailed_expense': detailed_expense
            })

        return jsonify(results)
    except Exception as e:
        return jsonify({'error: str(e)'}), 500

if __name__ == '__main__':
    app.run(debug=True)
