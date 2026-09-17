num1 = int(input("enter num1"))
num2 = int(input("enter num2"))
num3 = int(input("enter num3"))
if num1>num2 and num1>num3:
    print("maximum is",num1)
elif num2>num1 and num2>num3:
    print("maximum is",num2)
else:
    print("maximum is",num3)
