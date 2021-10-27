print("Welcome to BMI Calculator")
height = float(input("enter your height in m"))
weight = float(input("enter your weight in kg"))
bmi = weight / height**2
print(f"your BMI Index is at {bmi}")
if bmi < 18.5:
    print("they are underweight")
elif bmi <25:
    print("you are of normal weight")
elif bmi < 30:
    print("you are over weight")
elif bmi < 35:
    print("you are obese")
else:
    print("you are clinically obese,contact your Dr soon")