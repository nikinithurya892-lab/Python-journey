count = 1
safe_count = 0
failed_count =0 

while count <= 4:
   temp = float(input("enter the temperature"))
   if 200<temp and temp<850:
      print("engine",count,"is safe!")
      safe_count = safe_count + 1
   else:
     print("engine",count,"is requered maintanace!")
     failed_count = failed_count + 1
     
   count = count +1
print("num of safe engines",safe_count) 
print("num of fault engines",failed_count)
