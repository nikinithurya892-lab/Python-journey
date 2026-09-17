att = float(input("Enter attendance score "))
marks = float(input("Enter average marks "))
    
if att >= 80:
    if marks >= 75:
        print("Scholarship is awarded")
    else:
        print("Scholarship not awarded")
else:
    print("Insufficient attendance")
    