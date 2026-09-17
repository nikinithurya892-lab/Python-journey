data = [55,12,48,7,25,36,9,63,31,78]
max = data[0]

count = 1
while count <=9:
    if data[count] > max:
        max = data [count]
        count = count +1
print(max)


