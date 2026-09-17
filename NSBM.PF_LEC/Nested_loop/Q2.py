'''for i in range(1, 6):
    for j in range(i):
        print("*", end="")
    print()'''

i = 1

while i <= 5:
    j = 0
    
    while j < i:
        print("*", end="")
        j += 1
    
    print()
    i += 1