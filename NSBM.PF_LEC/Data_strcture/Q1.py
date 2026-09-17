#i can travel through this numbers using loop
#start - number
#end - 1
#iteration - reduce by 1

num = int(input("enter a number to find factorial? "))
fact = 1
while num>= 1:
   fact = fact * num
   num = num - 1
print(fact)

