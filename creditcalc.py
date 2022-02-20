import argparse
from math import log, ceil, pow, floor, prod

def overpayment_prod(loan_principal, monthly_payment, number_months=1):
    overpayment = monthly_payment * number_months - loan_principal
    print(f'Overpayment = {ceil(overpayment)}')

def annuity_payment_prod(loan_principal, number_months, loan_interest):
    monthly_interest_rate = loan_interest / 1200
    monthly_payment = ceil(loan_principal * monthly_interest_rate * pow((1 + monthly_interest_rate), number_months) / (pow((1 + monthly_interest_rate), number_months) - 1))
    print(f'Your annuity payment = {monthly_payment}!')
    overpayment_prod(loan_principal, monthly_payment, number_months)

def loan_principal_prod(monthly_payment, number_months, loan_interest):
    monthly_interest_rate = loan_interest / 1200
    loan_principal = monthly_payment / (monthly_interest_rate * pow((1 + monthly_interest_rate), number_months) / (pow((1 + monthly_interest_rate), number_months) - 1))
    print(f'Your loan principal = {floor(loan_principal)}!')
    overpayment_prod(loan_principal, monthly_payment, number_months)

def time_to_repay(loan_principal, monthly_payment, loan_interest):
    month_str, year_str = 'month', 'year'
    monthly_interest_rate = loan_interest / 1200
    number_months = ceil(log((monthly_payment / (monthly_payment - monthly_interest_rate * loan_principal)), (1 + monthly_interest_rate)))
    years, months = divmod(number_months, 12)
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
    print(f'It will take {time} to repay the loan!')
    overpayment_prod(loan_principal, monthly_payment, number_months)

def diff_payments_prod(loan_principal, number_months, loan_interest, month):
    monthly_interest_rate = loan_interest / 1200
    diff_payment = loan_principal / number_months + monthly_interest_rate * (loan_principal - loan_principal * (month - 1) / number_months)
    return ceil(diff_payment)

parser = argparse.ArgumentParser()

parser.add_argument('--type')
parser.add_argument('--principal', type=int)
parser.add_argument('--periods', type=int)
parser.add_argument('--interest', type=float)
parser.add_argument('--payment', type=int)

args = parser.parse_args()

type_var = ['annuity', 'diff']
type_diff = [args.principal, args.periods, args.interest]
type_annuity = [args.principal, args.payment, args.interest, args.periods]
elements = set(type_diff + type_annuity)
elements.discard(None)

if (args.type == 'annuity' and type_annuity.count(None) > 1
    or args.type == 'annuity' and not None in type_annuity
    or args.type == 'diff' and args.payment
    or args.type == 'diff' and None in type_diff
    or not args.type in type_var
    or not args.interest
    or prod(elements) < 0):
        print('Incorrect parameters.')
elif args.type == 'diff':
    stock = []
    for month in range(1, args.periods + 1):
        diff_payment = diff_payments_prod(args.principal, args.periods, args.interest, month)
        stock.append(diff_payment)
        print(f'Month {month}: payment is {diff_payment}')
    print()
    overpayment_prod(args.principal, sum(stock))
elif args.type == 'annuity':
    if not args.principal:
        loan_principal_prod(args.payment, args.periods, args.interest)
    if not args.periods:
        time_to_repay(args.principal, args.payment, args.interest)
    if not args.payment:
        annuity_payment_prod(args.principal, args.periods, args.interest)