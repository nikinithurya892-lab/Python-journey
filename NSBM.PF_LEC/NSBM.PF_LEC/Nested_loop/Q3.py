#Write a program to input 10 numbers from the user and calculate their total sum.

count = 1
total = 0

while count <= 10:
    num = int(input("Enter number "))
    total = total + num
    count = count + 1

print("Total sum =", total)