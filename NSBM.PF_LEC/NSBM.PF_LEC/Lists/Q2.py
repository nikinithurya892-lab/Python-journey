item_code = ["ITM001", "ITM002", "ITM007", "ITM003", "ITM004", "ITM005", "ITM006", "ITM008", "ITM009", "ITM0010"]
item_name = ["Rice", "Sugar", "Milk Powder", "Bread", "Eggs","Butter", "Tea", "Cooking Oil", "Soap", "Shampoo"]
item_price = [250, 280, 1450, 180, 520, 780, 650, 950, 220, 890]

print(f"{'code':<10} {'name':<15} {'price':<10}")
print("-" * 35)

for i in range(len(item_code)):
    print(f"{item_code[i]:<10} {item_name[i]:<15} {item_price[i]:<10}")

code = input("Item code ?")
qty = int(input("Enter Quantity ?"))

count=0
while count < 10:
    if item_code[count] == code:
       total = item_price[count] * qty
       print("Item:", item_name[count])
       print("Price:", item_price[count])
       print("Quantity:", qty)
       print("Total:", total)
    count = count + 1


