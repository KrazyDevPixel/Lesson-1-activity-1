height=float(input("Enter your height in centimeters: "))
weight=float(input("Enter your weight in kilograms: "))
bmi=weight/(height/100)**2
print("Your BMI is: "+str(round(bmi,2)))
if bmi<18.5:
    print("You are underweight")
elif 18.5<=bmi<25:
    print("You have a normal weight")
elif 25<=bmi<30:
    print("You are overweight")
elif 30<=bmi<35:
    print("You are obese")
else:
    print("You are clinically obese")
