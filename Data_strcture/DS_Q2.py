#A slaseman wants a programme to store his daily sales for one week.write a programme which allo user to enter sales on by one for 7 days and print it at end
#develop the above programme to print the total salemof the week

sales =[]

day = 1

while day <= 7:
    sale = float(input("enter sales?"))
    sales.append(sale)
    day = day + 1
print("sales of the week",sales)

#1.create an empty list
#a list stores many values
#we will store the sales for 7 days in the list

#2.start with day 1
#a variable called day is created
#it starts at 1

#3.repeat for 7 days
#while means repeat
#the loop continues as long as day is les than or equal to 7

#4.get the sales amount
#input() asks the user to type a value
#float() converts the value into a decimal number

#5.store the sales in the list
#apppend() adds the new sales value to the end of the list

#6.go to the next day
#this increase day by 1

#display all sales
#after all 7 days are entered,the program prints the list
