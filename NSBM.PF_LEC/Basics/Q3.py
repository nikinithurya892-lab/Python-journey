#Q3 Write the program to calculate the compound interest when customer enters principle amount, interest rate and number of years
p = float (input("Enter Ammount ? "))
i = float(input("Enter Intrest Rate ? "))
t = int(input("Enter years ? "))

        
invesment = p * ((100+i)/100)**t
intrest = invesment - p

print("Totle invesment is ", invesment)
print("Totle Compound Interest is ",intrest)  
