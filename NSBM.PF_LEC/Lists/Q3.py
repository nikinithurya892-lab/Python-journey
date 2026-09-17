medicine_code = ["MED001","MED002","MED003","MED004","MED005","MED006","MED007","MED008","MED009","MED010"]
medicine_name = ["Paracetamol","Vitamin C","Cough Syrup","Antacid","Pain Relief Gel","Face Mask Pack","Hand Sanitizer","Bandage Roll","Antibiotic Cream","Thermometer"]
medicine_price = [120,450,780,350,920,180,520,250,680,1500]
final_bill = 0

print(f"{'Code':<10}{'Name':<20}{'Qty':<10}{'Price':<10}{'Total':<10}")
print("-"*60)

while True:
    code = input("Enter Medicine Code: ").upper()
    found = False
    for i in range(len(medicine_code)):
        if code == medicine_code[i]:
            qty = int(input("Enter Quantity: "))
            total = qty * medicine_price[i]
            final_bill += total
            print(f"{medicine_code[i]:<10}{medicine_name[i]:<20}{qty:<10}{medicine_price[i]:<10}{total:<10}")
            found = True
            break
    if found == False:
        print("Medicine not found.")
    choice = input("Do you want to add another medicine? (Y/N): ").upper()
    if choice == "N":
        break
print("-"*60)
print("Final Bill Amount = Rs.", final_bill)


