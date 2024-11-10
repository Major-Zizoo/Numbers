Weight=float(input("Enter weight:"))
Height=float(input("Enter height"))

BMI=Weight/(Height/100)**2

print("BMI is",BMI)

if BMI <= 18.4:
    print("Underweight")
elif BMI <= 24.6:
    print("Healthy")
else:
    print("Not Healthy")