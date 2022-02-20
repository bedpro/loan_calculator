from math import log, ceil, pow, floor

CHOICE_1, CHOICE_2, CHOICE_3 = 'n', 'a', 'p'

user_choice = input(f'''What do you want to calculate?
type "{CHOICE_1}" for number of monthly payments,
type "{CHOICE_2}" for annuity monthly payment amount,
type "{CHOICE_3}" for loan principal:\n''')
month_str, year_str = 'month', 'year'

if user_choice != CHOICE_3:
    loan_principal = int(input('Enter the loan principal:\n'))
    if user_choice == CHOICE_1:
        monthly_payment = int(input('Enter the monthly payment:\n'))
        loan_interest = float(input('Enter the loan interest:\n'))
        monthly_interest_rate = loan_interest / 1200
        number_months = log((monthly_payment / (monthly_payment - monthly_interest_rate * loan_principal)), (1 + monthly_interest_rate))
        years, months = divmod(ceil(number_months), 12)
        if years and months:
            if months > 1:
                month_str += 's'
            if years > 1:
                year_str += 's'
            time = f'{years} {year_str} and {months} {month_str}'
        elif not years:
            if months > 1:
                month_str += 's'
            time = f'{months} {month_str}'
        elif not months:
            if years > 1:
                year_str += 's'
            time = f'{years} {year_str}'
        print(f'It will take {time} to repay the loan')
    elif user_choice == CHOICE_2:
        number_months = int(input('Enter the number of periods:\n'))
        loan_interest = float(input('Enter the loan interest:\n'))
        monthly_interest_rate = loan_interest / 1200
        monthly_payment = loan_principal * monthly_interest_rate * pow((1 + monthly_interest_rate), number_months) / (pow((1 + monthly_interest_rate), number_months) - 1)
        print(f'Your monthly payment = {ceil(monthly_payment)}!')
else:
    monthly_payment = float(input('Enter the annuity payment:\n'))
    number_months = int(input('Enter the number of periods:\n'))
    loan_interest = float(input('Enter the loan interest:\n'))
    monthly_interest_rate = loan_interest / 1200
    loan_principal = monthly_payment / (monthly_interest_rate * pow((1 + monthly_interest_rate), number_months) / (pow((1 + monthly_interest_rate), number_months) - 1))
    print(f'Your loan principal = {floor(loan_principal)}!')