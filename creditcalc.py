import math
# import sys
import argparse


# functions
# Calculate the nominal interest rate given a yearly interest rate
def nominal_interest_calc(yearly_interest_value):
    return yearly_interest_value / (12 * 100)


# calculate overpayments - how much you will pay in interest
def overpayment_calc(payments, periods, principal_amt):
    return (payments * periods) - principal_amt


# Collect arguments
parser = argparse.ArgumentParser(description="Credit Calculator")
parser.add_argument('-t', '--type', type=str, choices=['annuity', 'diff'],
                    help="Enter in 'annuity' or 'diff'")
parser.add_argument("-p", "--principal", type=float,
                    help="Enter in the principal amount")
parser.add_argument("-n", "--periods", type=int,
                    help="Enter in the number of periods in months")
parser.add_argument("-i", "--interest", type=float, default=0,
                    help="Enter in the yearly interest rate e.g. 12 (without a percentage sign")
parser.add_argument("-ps", "--payment", type=float,
                    help="Enter in the payment amount")

args = parser.parse_args()

# store arguments in variables
t = args.type
p = args.principal
n = args.periods
i = args.interest
if i == 0:
    # print("Error: Please enter the annual interest rate without % symbol.")
    print("Incorrect parameters")
    exit()
else:
    i = nominal_interest_calc(args.interest)
ps = args.payment

# Check type of calculation and calculate based on values
if t == "annuity":

    print("Calculating annuity payments...")

    if ps is None:
        annuity = math.ceil(p * (i * ((1 + i) ** n) / ((1 + i) ** n - 1)))
        print("Your annuity payment = {}!".format(annuity))
        print("Overpayment = {}".format(math.ceil(overpayment_calc(annuity, n, p))))

    elif p is None:
        aboveTheLine = i * (1 + i) ** n
        belowTheLine = (1 + i) ** n - 1
        allBelowLine = aboveTheLine / belowTheLine
        principal = ps / allBelowLine
        print("Your credit principle = {}!".format(int(principal)))
        print("Overpayment = {}".format(math.ceil(overpayment_calc(ps, n, principal))))

    elif n is None:
        x = ps / (ps - i * p)
        # print("x = {}".format(x))
        if x <= 0:
            print("Something went wrong: Check your inputs")
            exit()
        base = 1 + i
        num_months = math.log(x, base)
        # print("number of months: {}".format(num_months))
        n_months = math.ceil(num_months)
        # print("number of months (math.ceil): ", n_months)
        n_years, n_remaining_months = divmod(n_months, 12)
        if n_remaining_months == 0:
            print("You need {} years to repay this credit!".format(n_years))
        else:
            print("You need {} years and {} months to repay this credit!".format(n_years, n_remaining_months))

        print("Overpayment = {}".format(math.ceil(overpayment_calc(ps, n_months, p))))


elif t == "diff":
    if ps is not None:
        print("Oops! Looks like you added the monthly payment amount. Check if this is correct or select a different type of calculation e.g. (annuity)")
        exit()
    elif n is None or n <= 0:
        print("Oops! Something went wrong. Check the value for number of periods.")
        exit()

    print("Calculating differential payments...")

    total_payments = 0
    for m in range(1, n+1):
        monthly_payments = math.ceil((p / n) + (i * (p - (p * (m - 1) / n))))
        total_payments += monthly_payments
        print("Month {}: paid out {}".format(m, monthly_payments))

    print()
    print("Overpayment = {}".format(math.ceil(total_payments - p)))


else:
    print("Error: Please select 'type' as either 'annuity' or 'diff'. You entered {}.".format(type))
