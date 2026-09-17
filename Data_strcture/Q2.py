#write a programme to check a number is a prime number or not?

num = int(input("enter a number:"))
if num <= 1:
    print("not a prime number")
else:
    is_prime = True
    for i in range(2, num):
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        print("prime number")
    else:
        print("not a prime number")