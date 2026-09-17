item_code = ["ITM001", "ITM002", "ITM003", "ITM004", "ITM005"]
item_name = ["Rice", "Sugar", "Milk", "Bread", "Eggs"]
item_price = [250, 280, 1450, 180, 520]

print(f"{'code':<10} {'name':<15} {'price':<10}")
print("-" * 35)

for i in range(len(item_code)):
    print(f"{item_code[i]:<10} {item_name[i]:<15} {item_price[i]:<10}")
#Display the list of items in a formatted way

code = input("Item code ?")
qty = int(input("Enter Quantity ?"))

count = 0
while count < 5:#bcs,the poditions are 0,1,2,3,4 : =is used to condition the loop to run 5 times 
    if item_code[count] == code:#check the code entered by user is in the list or not
        tot = item_price[count] * qty
    count = count + 1
print("Total bill is",tot)

#f means Formatted String (or f-string)
 
#<10 means:
#Align the text to the left (<)
#Use 10 spaces for that value

#print("-" * 35)
#This prints a line of dashes
#ex:-----------------------

#len() means length
#There are 5 item codes.
