# Credit Calculator
A credit calculator using mathematics, python, 3rd party modules and; libraries. 

## About
Finance is an important part of the life of any people. Sometimes you think about getting additional income and want to open a deposit account. And sometimes you need additional money right now and want to take a credit or mortgage. Anyway, you may want to calculate different financial indicators to make a decision. Let’s make such an instrument that can help us.

# The rational for this project
To build upon and keep my python skills fresh but at the some time learn more about maths. 

## What I learnt
I learnt how to use mathematics and Python in everyday tasks, use third-party modules and libraries. Also, I learnt more about different financial instruments. I took all this knowledge and put it together creating a credit calculator. 

## How to run
Run the program from the command line passing in 4 of the 5 arguments. 
### Arguments
- type: annuity or diff
- principal: the amount to borrow (float or int)
- periods: the number of months (int) to payback the loan
- interest: they yearly interest rate (float) without the % symbol
- payment: the monthly payment amount (float)

## Examples from the command line
### Example 1 - Calculating the principal
> python credit_calc.py --type=annuity --payment=8722 --periods=120 --interest=5.6

Your credit principal = 800018!

Overpayment = 246622

### Example 2 - Calculating the time needed to pay back the loan
> python credit_calc.py --type=annuity --principal=500000 --payment=23000 --interest=7.8

You need 2 years to repay this credit!

Overpayment = 52000

### Example 3 - Calculating the differentiated payment 
> python credit_calc.py --type=diff --principal=500000 --periods=8 --interest=7.8

Month 1: paid out 65750

Month 2: paid out 65344

Month 3: paid out 64938

Month 4: paid out 64532

Month 5: paid out 64125

Month 6: paid out 63719

Month 7: paid out 63313

Month 8: paid out 62907

Overpayment = 14628

### Example 4 - Calculating the annuity payment
> python credit_calc.py --type=annuity --principal=1000000 --periods=60 --interest=10

Your annuity payment = 21248!

Overpayment = 274880




##### My thanks to JetBrains Academy
