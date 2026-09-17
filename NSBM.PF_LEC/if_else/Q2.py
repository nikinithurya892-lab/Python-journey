att = float(input("Enter attendance score "))

if att >= 80:
    marks = float(input("Enter average marks "))
    
    if marks >= 75:
        print("Scholarship is awarded")
    else:
        print("Scholarship not awarded")
else:
    print("Insufficient attendance")