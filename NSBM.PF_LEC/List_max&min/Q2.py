data = [87,-65,-4,14,-112]
min = data[0]

count = 1
while count <=5:
    if data[count]<min:
        min = data[count]

        count = count + 1

print(min)

