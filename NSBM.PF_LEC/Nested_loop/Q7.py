#Write a program to calculate and display the sum of all even numbers from 1 to 50 using a loop.

count = 2
sum = 0

while count <= 50:
    sum = sum + count
    count = count + 2

print("Sum of even numbers =", sum)
