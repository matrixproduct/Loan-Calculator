import math, sys
import argparse


def print_months(m_to_repay):
    years = m_to_repay // 12
    months = m_to_repay % 12
    end_y = 's' if years != 1 else ''
    end_m = 's' if months != 1 else ''
    years_str = f'{years} year{end_y}' if years else ''
    months_str = f'{months} month{end_m}' if months else ''
    and_str = ' and ' if years and months else ''
    print('It will take ' + years_str + and_str + months_str + ' to repay this loan!')


def print_overpayment(loan_principal, monthly_payment, months_to_repay):
    print('Overpayment =', int(monthly_payment * months_to_repay - loan_principal))


def cal_months_to_repay(loan_principal, monthly_payment, interest):
    i = interest * 0.01 / 12
    months_to_repay = math.ceil(math.log(monthly_payment / (monthly_payment - i * loan_principal), 1 + i))
    print_months(months_to_repay)
    print_overpayment(loan_principal, monthly_payment, months_to_repay)


def cal_monthly_payment(loan_principal, months_to_repay, interest):
    i = interest * 0.01 / 12
    monthly_payment = math.ceil(loan_principal * (i * (1+i) ** months_to_repay) / ((1+i) ** months_to_repay - 1))
    print(f'Your annuity payment = {monthly_payment}!')
    print_overpayment(loan_principal, monthly_payment, months_to_repay)


def cal_loan_principal(monthly_payment, months_to_repay, interest):
    i = interest * 0.01 / 12
    loan_principal = math.floor(monthly_payment * ((1+i) ** months_to_repay - 1) / (i * (1+i) ** months_to_repay))
    print(f'Your loan principal  = {loan_principal}!')
    print_overpayment(loan_principal, monthly_payment, months_to_repay)


def cal_diff_monthly_payment(loan_principal, months_to_repay, interest):
    i = interest * 0.01 / 12
    P = loan_principal; n = months_to_repay
    payments = []
    for m in range(1, n + 1):
        dm = math.ceil(P / n + i * P * (1 - (m - 1) / n))
        payments.append(dm)
        print(f'Month {m}: payment is', dm)
    print('\nOverpayment =', int(sum(payments) - P))


def handle_input():
    error_msg = 'Incorrect parameters'
    parser = argparse.ArgumentParser()
    parser.add_argument("--type", type=str, help="Can be either 'annuity' or 'diff'")
    parser.add_argument("--payment", type=int, help="If --type=diff, their combination is invalid")
    parser.add_argument("--principal", type=int, help="Valid with every combiantion")
    parser.add_argument("--periods", type=int, help="Denotes the number of months and/or years  needed to repay the credit")
    parser.add_argument("--interest", type=float, help="Must always be specified.")
    args = parser.parse_args()

    if args.type is None or args.interest is None or (args.type != 'annuity' and args.type != 'diff'):
        print(error_msg)
        sys.exit()
    if args.type == 'diff':
        if args.principal is None or args.periods is None or args.principal < 0 or args.periods < 0:
            print(error_msg)
            sys.exit()
        cal_diff_monthly_payment(args.principal, args.periods, args.interest)
    else:
        if args.periods is None and args.principal is not None and args.payment is not None and args.principal > 0 and args.payment > 0:
            cal_months_to_repay(args.principal, args.payment, args.interest)
        elif args.principal is None and args.periods is not None and args.payment is not None and args.periods > 0 and args.payment > 0:
            cal_loan_principal(args.payment, args.periods, args.interest)
        elif args.payment is None and args.periods is not None and args.principal is not None and args.periods > 0 and args.principal > 0:
            cal_monthly_payment(args.principal, args.periods, args.interest)
        else:
            print(error_msg)
            sys.exit()


handle_input()