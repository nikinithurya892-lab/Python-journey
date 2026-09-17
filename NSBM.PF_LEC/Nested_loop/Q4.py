#Write a program to input 5 numbers and display the largest number using a loop.

count = 1
largest = 0

while count <= 5:
    num = int(input("Enter number="))
    if num > largest:
        largest = num
    count = count + 1
    
print("largest num is=", largest)
