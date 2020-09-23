# Loan Calculator
 
Calculation of differentiated and annuity payments. For differentiated payments the user can run the program specifying interest, number of monthly payments, and loan principal.
For annuity payments: principal, number of monthly payments, and monthly payment amount. The user specifies all the known parameters with command-line arguments, and one parameter will be unknown. This is the value the user wants to calculate.


Examples:

python creditcalc.py --type=diff --principal=1000000 --periods=10 --interest=10

Month 1: payment is 108334

Month 2: payment is 107500

Month 3: payment is 106667

Month 4: payment is 105834

Month 5: payment is 105000

Month 6: payment is 104167

Month 7: payment is 103334

Month 8: payment is 102500

Month 9: payment is 101667

Month 10: payment is 100834

Overpayment = 45837


python creditcalc.py --type=annuity --principal=1000000 --periods=60 --interest=10
Your annuity payment = 21248!
Overpayment = 274880

python creditcalc.py --type=annuity --payment=8722 --periods=120 --interest=5.6
Your loan principal = 800018!
Overpayment = 246622

python creditcalc.py --type=annuity --principal=500000 --payment=23000 --interest=7.8
It will take 2 years to repay this loan!
Overpayment = 52000
