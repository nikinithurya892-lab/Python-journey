#Q4 A company wants a payroll system under following criterias
#.basic salary?
#.perfomance allowance = number of working days*(basic*5%)
#.For extra hours 250 per hour
#.12% of tax must be educated

n = float (input("Basic salary ? "))
l = int(input("num of working days ? "))
m = float (input("extra hours? "))

perfomance_allowance = l*(n*(5/100))
extra_hour_payment = m*250
salary = perfomance_allowance + extra_hour_payment
tax = salary*(12/100)

final = perfomance_allowance + extra_hour_payment - tax
print(final)

#Q5 A car company wants to system to calculate amount of few conseum,cost for the feul and total cost of the juorny when user enters distance traveled,


